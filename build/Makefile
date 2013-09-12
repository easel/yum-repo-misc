#OPTIONS="-r epel-5-x86_64 --no-cleanup-after --no-clean"
#OPTIONS="-r epel-5-x86_64 --no-clean"
#OPTIONS=-r epel-5-x86_64 --no-cleanup-after --offline --verbose
# for Centos5
# OPTIONS=-r epel-5-x86_64 --verbose

# for Centos6 
OPTIONS=-r epel-6-x86_64 --verbose

PYTHON27_OPTIONS=-r python27-x86_64 --no-cleanup-after --no-clean --verbose
RUBY193_OPTIONS=-r ruby193-x86_64 --no-cleanup-after --no-clean --verbose

ROOT=/home/vagrant/build
PHANTOMJS_VER=1.8.1-1


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

.PHONY: MySQL-python
MySQL-python:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/MySQL-python.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/MySQL-python-1.2.3-1.el6.src.rpm

.PHONY: python-mod_wsgi
python-mod_wsgi:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python-mod_wsgi.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-mod_wsgi-3.4-2.ius.src.rpm

.PHONY: python-pip
python-pip:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python-pip.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-pip-1.4.1-1.src.rpm


.PHONY: python-virtualenv
python-virtualenv:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python-virtualenv.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-virtualenv-1.7.2-2.src.rpm

.PHONY: rcov
rcov:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rcov.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	# mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/rcov-???.el6.src.rpm

