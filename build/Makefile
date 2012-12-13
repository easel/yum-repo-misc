#OPTIONS="-r epel-5-x86_64 --no-cleanup-after --no-clean"
#OPTIONS="-r epel-5-x86_64 --no-clean"
OPTIONS=-r epel-5-x86_64 --no-cleanup-after --offline --verbose
ROOT=/home/vagrant/build

nodejs:	
	#mock $(OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs-0.8.15-1.el5.centos.src.rpm
