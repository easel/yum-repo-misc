
EPEL_VERSION=6

#OPTIONS="-r epel-5-x86_64 --no-cleanup-after --no-clean"
#OPTIONS="-r epel-5-x86_64 --no-clean"
#OPTIONS=-r epel-5-x86_64 --no-cleanup-after --offline --verbose

# for Centos5
# OPTIONS=-r epel-5-x86_64 --verbose

# for Centos6
# OPTIONS=-r epel-6-x86_64 --verbose

# For universal build version
OPTIONS=-r epel-$(EPEL_VERSION)-x86_64


# used for building the build packages, like python27-build and ruby193-build
SCL_OPTIONS=-r scl-x86_64

# used for building python27 SCL-based packages
PYTHON27_OPTIONS=-r python27-x86_64 

# used for building python33 SCL-based packages
PYTHON33_OPTIONS=-r python33-x86_64 

# used for bulding ruby193 SCL-based packages
RUBY193_OPTIONS=-r ruby193-x86_64 

# used for bulding Postgres 9.2 SCL-based packages
POSTGRES92_OPTIONS=-r postgres92-x86_64  

# used for bulding Perl 5.16 SCL-based packages
PERL516_OPTIONS=-r perl516-x86_64 

# used for bulding Node 0.10 SCL-based packages
NODE010_OPTIONS=-r node010-x86_64 

# used for bulding PHP 5.4 SCL-based packages
PHP54_OPTIONS=-r php54-x86_64 

# used for bulding MySQL 5.5 SCL-based packages
MYSQL55_OPTIONS=-r mysql55-x86_64 

# used for bulding MariaDB 5.5 SCL-based packages
MARIADB55_OPTIONS=-r maria55db-x86_64 



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
	@echo "    [EPEL6 only] MARIADB55_OPTIONS=$(MARIADB55_OPTIONS)"
	@echo "    [EPEL6 only] MYSQL55_OPTIONS=$(MYSQL55_OPTIONS)"
	@echo "    [EPEL6 only] POSTGRES92_OPTIONS=$(POSTGRES92_OPTIONS)"
	@echo "    [EPEL6 only] PYTHON27_OPTIONS=$(PYTHON27_OPTIONS)"
	@echo "    [EPEL6 only] PYTHON33_OPTIONS=$(PYTHON33_OPTIONS)"
	@echo "    [EPEL6 only] RUBY193_OPTIONS=$(RUBY193_OPTIONS)"
	@echo "    [EPEL6 only] PERL516_OPTIONS=$(PERL516_OPTIONS)"
	@echo "    [EPEL6 only] NODE010_OPTIONS=$(NODE010_OPTIONS)"
	@echo "    [EPEL6 only] PHP54_OPTIONS=$(PHP54_OPTIONS)"
	@echo ""


# updates the repo
.PHONY: createrepo
createrepo:
	echo Updating epel-$(EPEL_VERSION) repository...
	mkdir -p ~/localrepo/epel/$(EPEL_VERSION)/x86_64/
	cp -v $(ROOT)/RPMS/*el$(EPEL_VERSION)*x86_64.rpm ~/localrepo/epel/$(EPEL_VERSION)/x86_64/
	cp -v $(ROOT)/RPMS/*el$(EPEL_VERSION)*noarch.rpm ~/localrepo/epel/$(EPEL_VERSION)/x86_64/
	createrepo ~/localrepo/epel/$(EPEL_VERSION)/x86_64/

.PHONY:
hdf5:
	mock $(OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/hdf5.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/hdf5-1.8.10-3.el$(EPEL_VERSION).src.rpm

.PHONY: ecryptfs-utils
.PHONY:
git:
	mock $(OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/git.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/git-1.8.2.1-1.el$(EPEL_VERSION).src.rpm

.PHONY: ecryptfs-utils
ecryptfs-utils:
	mock $(OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/ecryptfs-utils.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ecryptfs-utils-103-1.el$(EPEL_VERSION).centos.src.rpm

.PHONY: nodejs
nodejs:
	mock $(OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs-0.8.15-1.el$(EPEL_VERSION).centos.src.rpm

.PHONY: phantomjs
phantomjs: $(ROOT)/RPMS/phantomjs-$(PHANTOMJS_VER).el$(EPEL_VERSION).centos.x86_64.rpm

$(ROOT)/SRPMS/phantomjs-$(PHANTOMJS_VER).el$(EPEL_VERSION).centos.src.rpm: $(ROOT)/SPECS/phantomjs.spec
	mock $(OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/phantomjs.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS

$(ROOT)/RPMS/phantomjs-$(PHANTOMJS_VER).el$(EPEL_VERSION).centos.x86_64.rpm: $(ROOT)/SRPMS/phantomjs-$(PHANTOMJS_VER).el$(EPEL_VERSION).centos.src.rpm
	mock $(OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/phantomjs-1.8.1-1.el$(EPEL_VERSION).centos.src.rpm


##
##  INCLUDE THE SCL DEFINITIONS HERE
##
##  There are like 9 million of them, so why pollute this Makefile?
##

include Makefile-scl.mk

