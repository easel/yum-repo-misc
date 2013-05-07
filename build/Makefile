#OPTIONS="-r epel-5-x86_64 --no-cleanup-after --no-clean"
#OPTIONS="-r epel-5-x86_64 --no-clean"
#OPTIONS=-r epel-5-x86_64 --no-cleanup-after --offline --verbose
OPTIONS=-r epel-5-x86_64 --verbose
ROOT=/home/vagrant/build
PHANTOMJS_VER=1.8.1-1


.PHONY: 
hdf5:	
	mock $(OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/hdf5.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/hdf5-1.8.10-3.el5.centos.src.rpm

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


