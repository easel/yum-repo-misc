#! /bin/bash


# TODO: put the rpms in the right place so that it can be automatically added
# to the epel-easel


# per step 1 oo_notes_building_rpms_from_source.txt
#
# This is added to the origin mock config so we don't do it here 
#
# sudo yum install -y rubygem-thor git tito yum-plugin-priorities wget \
# vim-enhanced ruby-devel rubygems-devel rubygem-aws-sdk rubygem-parseconfig \
# rubygem-yard rubygem-redcarpet createrepo

# clone the origin-server repo
git clone https://github.com/openshift/origin-server

# From http://cloud-mechanic.blogspot.com/2013/03/the-bleeding-edge-building-openshift.html
# about 2/3 way down

# copy git repo in to the mock
mock -r origin-x86_64 --copyin origin-server /root/origin-server 

# for some reason, the rpmdb is not always right after a mock init. This
# forces it to not suck.
# 
mock -r origin-x86_64 --cwd=/root --shell 'rpmdb --rebuilddb; rpmdb --rebuilddb'

# build the packages ... do this by finding the specs, doing a yum-builddep 
# against them to suck in any necessary dependencies, then tito'ing the 
# spec to make an rpm. They'll all end up in /tmp/tito-result in the 
# mock env.
#
mock -r origin-x86_64 --shell 'mkdir -p /tmp/tito-result; for PKGDIR in \$(find origin-server -name \*.spec | xargs -i{} dirname {});  do (cd \$PKGDIR; yum-builddep -y *.spec; tito build -o /tmp/tito-result --rpm); done'

# Pull them out of the mock environment and back onto our non-chrooted 
# space ... I tried copyout but got selinux errors, and this works. 
#
mkdir -p /home/vagrant/tito-cache
cd /var/lib/mock/origin-x86_64/root/tmp/tito-result/
find . -name \*rpm | cpio -dpmv /home/vagrant/tito-cache

# after this, check out gh pages and push them into the repo
#
echo OK, now you can move the rpms from tito-cache into the gh-pages/epel 
echo space.
