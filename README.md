A collection of RPMS

To use this repo, create a file /etc/yum.repos.d/epel-easel.repo with the following in it:

[epel-easel]
name=Easel EPEL
baseurl=http://easel.github.com/yum-repo-misc/epel/5/x86_64/
enabled=1
gpgcheck=0
priority=99
