
EPEL_VERSION=6

#OPTIONS="-r epel-5-x86_64 --no-cleanup-after --no-clean"
#OPTIONS="-r epel-5-x86_64 --no-clean"
#OPTIONS=-r epel-5-x86_64 --no-cleanup-after --offline --verbose

# for Centos5
# OPTIONS=-r epel-5-x86_64 --verbose

# for Centos6 
# OPTIONS=-r epel-6-x86_64 --verbose

# For universal build version
OPTIONS=-r epel-$(EPEL_VERSION)-x86_64 --verbose


# used for building the build packages, like python27-build and ruby193-build
SCL_OPTIONS=-r scl-x86_64 

# used for building python27 SCL-based packages
PYTHON27_OPTIONS=-r python27-x86_64 

# used for bulding ruby193 SCL-based packages
RUBY193_OPTIONS=-r ruby193-x86_64 

ROOT=/home/vagrant/build
PHANTOMJS_VER=1.8.1-1

.PHONY:
default:
	@echo Build RPM packages for Easel repo
	@echo
	@echo To build epel-5 packages, use make EPEL_VERSION=5 makeid
	@echo to build epel-6 packages, use make EPEL_VERSION=6 makeid
	@echo
	@echo defaults:
	@echo
	@echo "                 OPTIONS=$(OPTIONS)"
	@echo "    [EPEL6 only] SCL_OPTIONS=$(SCL_OPTIONS)"
	@echo "    [EPEL6 only] PYTHON27_OPTIONS=$(PYTHON27_OPTIONS)" 
	@echo "    [EPEL6 only] RUBY193_OPTIONS=$(RUBY193_OPTIONS)"
	@echo ""


# updates the repo
.PHONY: createrepo
createrepo:
	echo Updating epel-$(EPEL_VERSION) repository...
	mkdir -p ~/localrepo/epel/$(EPEL_VERSION)/x86_64/
	cp -v $(ROOT)/RPMS/*el$(EPEL_VERSION)*x86_64.rpm ~/localrepo/epel/$(EPEL_VERSION)/x86_64/
	createrepo ~/localrepo/epel/$(EPEL_VERSION)/x86_64/
	
.PHONY: 
hdf5:	
	mock $(OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/hdf5.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/hdf5-1.8.10-3.el6.centos.src.rpm

.PHONY: ecryptfs-utils
.PHONY: 
git:	
	mock $(OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/git.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/git-1.8.2.1-1.el5.centos.src.rpm

.PHONY: ecryptfs-utils
ecryptfs-utils:	
	mock $(OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/ecryptfs-utils.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ecryptfs-utils-103-1.el5.centos.src.rpm

.PHONY: nodejs
nodejs:	
	mock $(OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs-0.8.15-1.el5.centos.src.rpm

.PHONY: phantomjs
phantomjs: $(ROOT)/RPMS/phantomjs-$(PHANTOMJS_VER).el5.centos.x86_64.rpm

$(ROOT)/SRPMS/phantomjs-$(PHANTOMJS_VER).el5.centos.src.rpm: $(ROOT)/SPECS/phantomjs.spec
	mock $(OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/phantomjs.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS

$(ROOT)/RPMS/phantomjs-$(PHANTOMJS_VER).el5.centos.x86_64.rpm: $(ROOT)/SRPMS/phantomjs-$(PHANTOMJS_VER).el5.centos.src.rpm
	mock $(OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/phantomjs-1.8.1-1.el5.centos.src.rpm

# These are the actual python27, python27-build and python27-python packages
# This will also update the repository with the package in it, because it's a dependency for everyone else

.PHONY: python27
python27:
	mock $(SCL_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(SCL_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-1-3.el6.src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python
python27-python:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-2.7.3-16.el6.src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo


# These are the python27 module packages themselves

.PHONY: MySQL-python
MySQL-python:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/MySQL-python.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-MySQL-python-1.2.3-1.el6.src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python-mod_wsgi
python-mod_wsgi:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python-mod_wsgi.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-mod_wsgi-3.4-2.ius.el6.src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python-pip
python-pip:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python-pip.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-pip-1.4.1-1.el6.src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python-virtualenv
python-virtualenv:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python-virtualenv.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-virtualenv-1.7.2-2.el6.src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo



# These are the actual ruby193, ruby193-build, and ruby193-ruby packages
# This will also update the local repository to put the package(s) out in 
# that repo, because other builds will depend on it being available

.PHONY: ruby193
ruby193:
	mock $(SCL_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/ruby193.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(SCL_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-1-6.el6.src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-libyaml
ruby193-libyaml:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/libyaml.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-libyaml-0.1.4-4.el6.src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-ruby 
ruby193-ruby:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/ruby.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-ruby-1.9.3.327-27.el6.src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

# These are the actual ruby 193 rubygems. 

.PHONY: ruby193-rubygem-rcov
ruby193-rubygem-rcov:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rcov.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-rcov-0.9.9-9.el6.src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

