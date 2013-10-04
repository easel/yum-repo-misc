#
#
# Makefile for SCL-related stuff
#
#

# SCL metapackages

.PHONY: all-scl-meta
all-scl-meta: python27 python33 postgres92 mysql55 mariadb55 \
	nodejs010 perl516 php54 ruby193



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Generic support, like scl-utils
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

.PHONY: scl-utils
scl-utils:
	mock $(OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/scl-utils.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/scl-utils-20120927-8.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Maria DB 5.5
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


.PHONY: mariadb55
mariadb55:
	mock $(SCL_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/mariadb55.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(SCL_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/mariadb55-1-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: mariadb55-mariadb
mariadb55-mariadb:
	mock $(MARIADB55_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/mariadb55-mariadb.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(MARIADB55_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/mariadb55-mariadb-5.5.32-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# MySQL 5.5
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

.PHONY: mysql55
mysql55:
	mock $(SCL_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/mysql55.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(SCL_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/mysql55-1-14.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: mysql55-mysql
mysql55-mysql:
	mock $(MYSQL55_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/mysql55-mysql.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(MYSQL55_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/mysql55-mysql-5.5.32-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# NODE.js 0.10
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


.PHONY: nodejs010-all
nodejs010-all: nodejs010 nodejs010-v8 nodejs010-c-ares nodejs010-gyp \
	nodejs010-http-parser nodejs010-libuv nodejs010-nodejs nodejs010-npm \
	nodejs010-nodejs-abbrev \
	nodejs010-nodejs-ansi \
	nodejs010-nodejs-archy \
	nodejs010-nodejs-async \
	nodejs010-nodejs-aws-sign \
	nodejs010-nodejs-block-stream \
	nodejs010-nodejs-boom \
	nodejs010-nodejs-chmodr \
	nodejs010-nodejs-chownr \
	nodejs010-nodejs-combined-stream \
	nodejs010-nodejs-config-chain \
	nodejs010-nodejs-couch-login \
	nodejs010-nodejs-cryptiles \
	nodejs010-nodejs-delayed-stream \
	nodejs010-nodejs-forever-agent \
	nodejs010-nodejs-form-data \
	nodejs010-nodejs-fstream \
	nodejs010-nodejs-fstream-ignore \
	nodejs010-nodejs-fstream-npm \
	nodejs010-nodejs-glob \
	nodejs010-nodejs-graceful-fs \
	nodejs010-nodejs-hawk \
	nodejs010-nodejs-hoek \
	nodejs010-nodejs-inherits \
	nodejs010-nodejs-ini \
	nodejs010-nodejs-init-package-json \
	nodejs010-nodejs-json-stringify-safe \
	nodejs010-nodejs-lockfile \
	nodejs010-nodejs-lru-cache \
	nodejs010-nodejs-mime \
	nodejs010-nodejs-minimatch \
	nodejs010-nodejs-mkdirp \
	nodejs010-nodejs-mute-stream \
	nodejs010-nodejs-node-uuid \
	nodejs010-nodejs-nopt \
	nodejs010-nodejs-npmconf \
	nodejs010-nodejs-npmlog \
	nodejs010-nodejs-npm-registry-client \
	nodejs010-nodejs-oauth-sign \
	nodejs010-nodejs-once \
	nodejs010-nodejs-opener \
	nodejs010-nodejs-osenv \
	nodejs010-nodejs-promzard \
	nodejs010-nodejs-proto-list \
	nodejs010-nodejs-qs \
	nodejs010-nodejs-read \
	nodejs010-nodejs-read-installed \
	nodejs010-nodejs-read-package-json \
	nodejs010-nodejs-request \
	nodejs010-nodejs-retry \
	nodejs010-nodejs-rimraf \
	nodejs010-nodejs-semver \
	nodejs010-nodejs-sigmund \
	nodejs010-nodejs-slide \
	nodejs010-nodejs-sntp \
	nodejs010-nodejs-tar \
	nodejs010-nodejs-tobi-cookie \
	nodejs010-nodejs-tunnel-agent \
	nodejs010-nodejs-uid-number \
	nodejs010-nodejs-which


.PHONY: nodejs010
nodejs010:
	mock $(SCL_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs010.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(SCL_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-1-17.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-v8
nodejs010-v8:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/v8.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-v8-3.14.5.10-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-c-ares
nodejs010-c-ares:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/c-ares.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-c-ares-1.9.1-5.1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-gyp
nodejs010-gyp:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/gyp.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-gyp-0.1-0.9.1010svn.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-http-parser
nodejs010-http-parser:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/http-parser.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-http-parser-2.0-5.20121128gitcd01361.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-libuv
nodejs010-libuv:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/libuv.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-libuv-0.10.5-1.1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs
nodejs010-nodejs:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-0.10.5-6.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-npm
nodejs010-npm:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/npm.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-npm-1.2.17-9.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


.PHONY: nodejs010-node-gyp
nodejs010-node-gyp:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/node-gyp.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-node-gyp-0.9.5-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-abbrev
nodejs010-nodejs-abbrev:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-abbrev.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-abbrev-1.0.4-4.1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-ansi
nodejs010-nodejs-ansi:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-ansi.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-ansi-0.1.2-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-archy
nodejs010-nodejs-archy:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-archy.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-archy-0.0.2-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-async
nodejs010-nodejs-async:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-async.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-async-0.2.6-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-aws-sign
nodejs010-nodejs-aws-sign:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-aws-sign.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-aws-sign-0.2.0-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-block-stream
nodejs010-nodejs-block-stream:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-block-stream.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-block-stream-0.0.6-6.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-boom
nodejs010-nodejs-boom:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-boom.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-boom-0.4.0-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-chmodr
nodejs010-nodejs-chmodr:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-chmodr.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-chmodr-0.1.0-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-chownr
nodejs010-nodejs-chownr:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-chownr.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-chownr-0.0.1-8.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-combined-stream
nodejs010-nodejs-combined-stream:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-combined-stream.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-combined-stream-0.0.4-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-config-chain
nodejs010-nodejs-config-chain:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-config-chain.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-config-chain-1.1.5-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-couch-login
nodejs010-nodejs-couch-login:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-couch-login.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-couch-login-0.1.15-4.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-cryptiles
nodejs010-nodejs-cryptiles:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-cryptiles.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-cryptiles-0.2.0-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-delayed-stream
nodejs010-nodejs-delayed-stream:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-delayed-stream.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-delayed-stream-0.0.5-4.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-forever-agent
nodejs010-nodejs-forever-agent:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-forever-agent.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-forever-agent-0.2.0-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-form-data
nodejs010-nodejs-form-data:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-form-data.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-form-data-0.0.7-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-fstream
nodejs010-nodejs-fstream:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-fstream.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-fstream-0.1.22-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-fstream-ignore
nodejs010-nodejs-fstream-ignore:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-fstream-ignore.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-fstream-ignore-0.0.6-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-fstream-npm
nodejs010-nodejs-fstream-npm:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-fstream-npm.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-fstream-npm-0.1.4-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-glob
nodejs010-nodejs-glob:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-glob.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-glob-3.1.21-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-graceful-fs
nodejs010-nodejs-graceful-fs:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-graceful-fs.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-graceful-fs-1.2.1-2.1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-hawk
nodejs010-nodejs-hawk:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-hawk.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-hawk-0.12.1-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-hoek
nodejs010-nodejs-hoek:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-hoek.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-hoek-0.8.1-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-inherits
nodejs010-nodejs-inherits:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-inherits.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-inherits-1.0.0-8.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-ini
nodejs010-nodejs-ini:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-ini.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-ini-1.1.0-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-init-package-json
nodejs010-nodejs-init-package-json:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-init-package-json.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-init-package-json-0.0.7-5.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-json-stringify-safe
nodejs010-nodejs-json-stringify-safe:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-json-stringify-safe.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-json-stringify-safe-4.0.0-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-lockfile
nodejs010-nodejs-lockfile:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-lockfile.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-lockfile-0.3.0-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-lru-cache
nodejs010-nodejs-lru-cache:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-lru-cache.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-lru-cache-2.3.0-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-mime
nodejs010-nodejs-mime:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-mime.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-mime-1.2.9-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-minimatch
nodejs010-nodejs-minimatch:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-minimatch.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-minimatch-0.2.11-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-mkdirp
nodejs010-nodejs-mkdirp:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-mkdirp.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-mkdirp-0.3.5-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-mute-stream
nodejs010-nodejs-mute-stream:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-mute-stream.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-mute-stream-0.0.3-5.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-node-uuid
nodejs010-nodejs-node-uuid:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-node-uuid.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-node-uuid-1.4.0-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-nopt
nodejs010-nodejs-nopt:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-nopt.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-nopt-2.1.1-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-npmconf
nodejs010-nodejs-npmconf:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-npmconf.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-npmconf-0.0.23-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-npmlog
nodejs010-nodejs-npmlog:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-npmlog.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-npmlog-0.0.2-4.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-npm-registry-client
nodejs010-nodejs-npm-registry-client:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-npm-registry-client.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-npm-registry-client-0.2.20-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-oauth-sign
nodejs010-nodejs-oauth-sign:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-oauth-sign.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-oauth-sign-0.2.0-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-once
nodejs010-nodejs-once:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-once.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-once-1.1.1-4.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-opener
nodejs010-nodejs-opener:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-opener.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-opener-1.3.0-6.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-osenv
nodejs010-nodejs-osenv:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-osenv.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-osenv-0.0.3-4.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-promzard
nodejs010-nodejs-promzard:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-promzard.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-promzard-0.2.0-5.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-proto-list
nodejs010-nodejs-proto-list:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-proto-list.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-proto-list-1.2.2-4.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-qs
nodejs010-nodejs-qs:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-qs.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-qs-0.5.6-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-read
nodejs010-nodejs-read:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-read.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-read-1.0.4-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-read-installed
nodejs010-nodejs-read-installed:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-read-installed.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-read-installed-0.1.1-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-read-package-json
nodejs010-nodejs-read-package-json:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-read-package-json.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-read-package-json-0.3.0-4.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-request
nodejs010-nodejs-request:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-request.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-request-2.16.6-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-retry
nodejs010-nodejs-retry:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-retry.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-retry-0.6.0-4.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-rimraf
nodejs010-nodejs-rimraf:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-rimraf.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-rimraf-2.1.4-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-semver
nodejs010-nodejs-semver:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-semver.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-semver-1.1.4-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-sigmund
nodejs010-nodejs-sigmund:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-sigmund.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-sigmund-1.0.0-4.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-slide
nodejs010-nodejs-slide:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-slide.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-slide-1.1.3-6.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-sntp
nodejs010-nodejs-sntp:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-sntp.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-sntp-0.2.1-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-tar
nodejs010-nodejs-tar:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-tar.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-tar-0.1.17-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-tobi-cookie
nodejs010-nodejs-tobi-cookie:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-tobi-cookie.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-tobi-cookie-0.2.0-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-tunnel-agent
nodejs010-nodejs-tunnel-agent:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-tunnel-agent.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-tunnel-agent-0.2.0-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-uid-number
nodejs010-nodejs-uid-number:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-uid-number.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-uid-number-0.0.3-6.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: nodejs010-nodejs-which
nodejs010-nodejs-which:
	mock $(NODE010_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/nodejs-which.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(NODE010_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/nodejs010-nodejs-which-1.0.5-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Perl 5.16
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

.PHONY: perl516
perl516:
	mock $(SCL_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl516.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(SCL_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-1-11.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl
perl516-perl:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-5.16.3-12.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

.PHONY: perl516-perl-Archive-Tar
perl516-perl-Archive-Tar:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Archive-Tar.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Archive-Tar-1.90-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-autodie
perl516-perl-autodie:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-autodie.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-autodie-2.16-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-B-Lint
perl516-perl-B-Lint:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-B-Lint.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-B-Lint-1.17-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Carp
perl516-perl-Carp:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Carp.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Carp-1.26-101.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-CGI
perl516-perl-CGI:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-CGI.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-CGI-3.63-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Class-Inspector
perl516-perl-Class-Inspector:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Class-Inspector.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Class-Inspector-1.28-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Clone
perl516-perl-Clone:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Clone.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Clone-0.34-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Compress-Raw-Bzip2
perl516-perl-Compress-Raw-Bzip2:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Compress-Raw-Bzip2.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Compress-Raw-Bzip2-2.060-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Compress-Raw-Zlib
perl516-perl-Compress-Raw-Zlib:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Compress-Raw-Zlib.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Compress-Raw-Zlib-2.060-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-CPAN-Meta
perl516-perl-CPAN-Meta:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-CPAN-Meta.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-CPAN-Meta-2.120921-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-CPAN-Meta-Requirements
perl516-perl-CPAN-Meta-Requirements:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-CPAN-Meta-Requirements.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-CPAN-Meta-Requirements-2.122-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-CPAN-Meta-YAML
perl516-perl-CPAN-Meta-YAML:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-CPAN-Meta-YAML.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-CPAN-Meta-YAML-0.008-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Data-Dumper
perl516-perl-Data-Dumper:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Data-Dumper.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Data-Dumper-2.145-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Data-Peek
perl516-perl-Data-Peek:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Data-Peek.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Data-Peek-0.38-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-DBD-MySQL
perl516-perl-DBD-MySQL:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-DBD-MySQL.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-DBD-MySQL-4.023-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-DBD-Pg
perl516-perl-DBD-Pg:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-DBD-Pg.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-DBD-Pg-2.19.3-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-DBD-SQLite
perl516-perl-DBD-SQLite:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-DBD-SQLite.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-DBD-SQLite-1.29-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-DBI
perl516-perl-DBI:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-DBI.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-DBI-1.627-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-DBIx-Simple
perl516-perl-DBIx-Simple:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-DBIx-Simple.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-DBIx-Simple-1.35-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Devel-StackTrace
perl516-perl-Devel-StackTrace:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Devel-StackTrace.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Devel-StackTrace-1.30-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Devel-Symdump
perl516-perl-Devel-Symdump:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Devel-Symdump.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Devel-Symdump-2.10-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Digest
perl516-perl-Digest:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Digest.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Digest-1.17-100.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Digest-SHA
perl516-perl-Digest-SHA:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Digest-SHA.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Digest-SHA-5.84-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Encode
perl516-perl-Encode:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Encode.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Encode-2.51-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-ExtUtils-MakeMaker
perl516-perl-ExtUtils-MakeMaker:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-ExtUtils-MakeMaker.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-ExtUtils-MakeMaker-6.66-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-ExtUtils-Manifest
perl516-perl-ExtUtils-Manifest:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-ExtUtils-Manifest.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-ExtUtils-Manifest-1.61-100.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-FCGI
perl516-perl-FCGI:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-FCGI.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-FCGI-0.74-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-File-CheckTree
perl516-perl-File-CheckTree:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-File-CheckTree.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-File-CheckTree-4.42-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-File-Copy-Recursive
perl516-perl-File-Copy-Recursive:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-File-Copy-Recursive.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-File-Copy-Recursive-0.38-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-File-ShareDir
perl516-perl-File-ShareDir:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-File-ShareDir.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-File-ShareDir-1.03-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Filter
perl516-perl-Filter:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Filter.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Filter-1.49-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-IO-Compress
perl516-perl-IO-Compress:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-IO-Compress.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-IO-Compress-2.060-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-IO-String
perl516-perl-IO-String:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-IO-String.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-IO-String-1.08-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-IPC-Cmd
perl516-perl-IPC-Cmd:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-IPC-Cmd.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-IPC-Cmd-0.80-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-IPC-Run3
perl516-perl-IPC-Run3:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-IPC-Run3.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-IPC-Run3-0.045-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-JSON-PP
perl516-perl-JSON-PP:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-JSON-PP.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-JSON-PP-2.27202-100.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Locale-Codes
perl516-perl-Locale-Codes:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Locale-Codes.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Locale-Codes-3.25-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Log-Message
perl516-perl-Log-Message:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Log-Message.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Log-Message-0.08-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Module-Build
perl516-perl-Module-Build:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Module-Build.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Module-Build-0.40.05-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Module-Metadata
perl516-perl-Module-Metadata:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Module-Metadata.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Module-Metadata-1.000016-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Module-Pluggable
perl516-perl-Module-Pluggable:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Module-Pluggable.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Module-Pluggable-4.7-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Net-Daemon
perl516-perl-Net-Daemon:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Net-Daemon.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Net-Daemon-0.48-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Number-Compare
perl516-perl-Number-Compare:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Number-Compare.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Number-Compare-0.03-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Params-Check
perl516-perl-Params-Check:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Params-Check.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Params-Check-0.36-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-parent
perl516-perl-parent:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-parent.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-parent-0.225-100.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Parse-CPAN-Meta
perl516-perl-Parse-CPAN-Meta:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Parse-CPAN-Meta.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Parse-CPAN-Meta-1.4404-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-PathTools
perl516-perl-PathTools:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-PathTools.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-PathTools-3.40-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Perl-OSType
perl516-perl-Perl-OSType:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Perl-OSType.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Perl-OSType-1.003-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-PlRPC
perl516-perl-PlRPC:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-PlRPC.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-PlRPC-0.2020-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Pod-Checker
perl516-perl-Pod-Checker:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Pod-Checker.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Pod-Checker-1.60-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Pod-Coverage
perl516-perl-Pod-Coverage:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Pod-Coverage.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Pod-Coverage-0.23-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-podlators
perl516-perl-podlators:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-podlators.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-podlators-2.5.1-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Pod-Parser
perl516-perl-Pod-Parser:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Pod-Parser.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Pod-Parser-1.60-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Pod-Perldoc
perl516-perl-Pod-Perldoc:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Pod-Perldoc.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Pod-Perldoc-3.20-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Pod-Usage
perl516-perl-Pod-Usage:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Pod-Usage.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Pod-Usage-1.61-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Probe-Perl
perl516-perl-Probe-Perl:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Probe-Perl.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Probe-Perl-0.02-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Scalar-List-Utils
perl516-perl-Scalar-List-Utils:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Scalar-List-Utils.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Scalar-List-Utils-1.27-100.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Socket
perl516-perl-Socket:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Socket.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Socket-2.009-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Sys-Syslog
perl516-perl-Sys-Syslog:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Sys-Syslog.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Sys-Syslog-0.32-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Taint-Runtime
perl516-perl-Taint-Runtime:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Taint-Runtime.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Taint-Runtime-0.03-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Term-UI
perl516-perl-Term-UI:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Term-UI.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Term-UI-0.34-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Test-CPAN-Meta
perl516-perl-Test-CPAN-Meta:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Test-CPAN-Meta.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Test-CPAN-Meta-0.23-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Test-NoWarnings
perl516-perl-Test-NoWarnings:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Test-NoWarnings.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Test-NoWarnings-1.04-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Test-Pod
perl516-perl-Test-Pod:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Test-Pod.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Test-Pod-1.48-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Test-Pod-Coverage
perl516-perl-Test-Pod-Coverage:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Test-Pod-Coverage.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Test-Pod-Coverage-1.08-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Test-Requires
perl516-perl-Test-Requires:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Test-Requires.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Test-Requires-0.06-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Test-Script
perl516-perl-Test-Script:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Test-Script.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Test-Script-1.07-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Test-Tester
perl516-perl-Test-Tester:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Test-Tester.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Test-Tester-0.108-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Text-Glob
perl516-perl-Text-Glob:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Text-Glob.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Text-Glob-0.09-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Text-Soundex
perl516-perl-Text-Soundex:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Text-Soundex.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Text-Soundex-3.04-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Text-Unidecode
perl516-perl-Text-Unidecode:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Text-Unidecode.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Text-Unidecode-0.04-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Thread-Queue
perl516-perl-Thread-Queue:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Thread-Queue.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Thread-Queue-3.02-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-threads
perl516-perl-threads:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-threads.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-threads-1.86-100.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-threads-shared
perl516-perl-threads-shared:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-threads-shared.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-threads-shared-1.43-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Tie-IxHash
perl516-perl-Tie-IxHash:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Tie-IxHash.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Tie-IxHash-1.22-10.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-version
perl516-perl-version:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-version.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-version-0.99.02-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-Version-Requirements
perl516-perl-Version-Requirements:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-Version-Requirements.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-Version-Requirements-0.101022-100.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: perl516-perl-YAML
perl516-perl-YAML:
	mock $(PERL516_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/perl-YAML.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PERL516_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/perl516-perl-YAML-0.84-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# PHP 5.4
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


.PHONY: php54-all
php54-all: php54 php54-php php54-php-pear php54-php-pecl-apc \
	php54-php-pecl-memcache


.PHONY: php54
php54:
	mock $(SCL_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/php54.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(SCL_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/php54-1-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: php54-php
php54-php:
	mock $(PHP54_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/php54-php.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PHP54_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/php54-php-5.4.16-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

.PHONY: php54-php-pear
php54-php-pear:
	mock $(PHP54_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/php54-php-pear.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PHP54_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/php54-php-pear-1.9.4-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: php54-php-pecl-apc
php54-php-pecl-apc:
	mock $(PHP54_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/php54-php-pecl-apc.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PHP54_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/php54-php-pecl-apc-3.1.15-0.2.svn329724.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: php54-php-pecl-memcache
php54-php-pecl-memcache:
	mock $(PHP54_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/php54-php-pecl-memcache.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PHP54_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/php54-php-pecl-memcache-3.0.8-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Postgres 9.2
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

.PHONY: postgresql92-all
postgresql92-all: postgresql92 postgresql92-postgresql


.PHONY: postgresql92
postgresql92:
	mock $(SCL_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/postgresql92.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(SCL_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/postgresql92-1-12.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: postgresql92-postgresql
postgresql92-postgresql:
	mock $(POSTGRES92_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/postgresql.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(POSTGRES92_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/postgresql-9.2.4-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Python 2.7
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


.PHONY: python27-all
python27-all: python27 python27-python python27-python-setuptools \
	python27-python-docutils python27-MySQL-python python27-python-coverage \
	python27-python-markupsafe python27-python-nose python27-python-jinja2 \
	python27-babel python27-python-sphinx python27-python-pip \
	python27-python-pygments python27-python-virtualenv python27-mod_wsgi \
	python27-python-psycopg2


.PHONY: python27
python27:
	mock $(SCL_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(SCL_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-1-10.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python
python27-python:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-python.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-2.7.5-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

.PHONY: python27-babel
python27-babel:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/babel.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-babel-0.9.6-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-MySQL-python
python27-MySQL-python:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/MySQL-python.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-MySQL-python-1.2.3-9.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python-coverage
python27-python-coverage:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-coverage.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-coverage-3.5.3-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python-docutils
python27-python-docutils:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-docutils.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-docutils-0.10-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python-jinja2
python27-python-jinja2:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-jinja2.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-jinja2-2.6-9.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python-markupsafe
python27-python-markupsafe:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-markupsafe.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-markupsafe-0.11-11.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-mod_wsgi
python27-mod_wsgi:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-mod_wsgi.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-mod_wsgi-3.4-2.ius.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python-nose
python27-python-nose:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-nose.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-nose-1.2.1-6.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python-pip
python27-python-pip:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-pip.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-pip-1.4.1-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python-psycopg2
python27-python-psycopg2:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-psycopg2.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-psycopg2-2.4.5-9.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python-pygments
python27-python-pygments:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-pygments.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-pygments-1.5-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python-setuptools
python27-python-setuptools:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-setuptools.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-setuptools-0.6.28-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python-simplejson
python27-python-simplejson:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-simplejson.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-simplejson-3.0.5-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python-sphinx
python27-python-sphinx:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-sphinx.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-sphinx-1.1.3-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python-sqlalchemy
python27-python-sqlalchemy:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-sqlalchemy.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-sqlalchemy-0.7.9-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python-virtualenv
python27-python-virtualenv:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-virtualenv.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-virtualenv-1.10.1-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python27-python-werkzeug
python27-python-werkzeug:
	mock $(PYTHON27_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python27-werkzeug.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON27_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python27-python-werkzeug-0.8.3-5.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Python 3.3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


.PHONY: python33-python-all
python33-all: python33 python33-python python33-python-setuptools \
	python33-python-docutils python33-python-coverage \
	python33-python-markupsafe python33-python-nose python33-python-jinja2 \
  python33-python-sphinx python33-python-pip \
	python33-python-pygments python33-python-virtualenv \
	python33-python-simplejson python33-python-sqlalchemy \
	python33-mod_wsgi python33-python-psycopg2


.PHONY: python33
python33:
	mock $(SCL_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(SCL_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-1-6.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python33-python
python33-python:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-python.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-python-3.3.2-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

.PHONY: python33-python-coverage
python33-python-coverage:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-coverage.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-python-coverage-3.5.3-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python33-python-docutils
python33-python-docutils:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-docutils.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-python-docutils-0.10-4.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python33-python-jinja2
python33-python-jinja2:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-jinja2.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-python-jinja2-2.6-10.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python33-python-markupsafe
python33-python-markupsafe:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-markupsafe.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-python-markupsafe-0.11-10.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python33-mod_wsgi
python33-mod_wsgi:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-mod_wsgi.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-mod_wsgi-3.4-2.ius.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python33-python-nose
python33-python-nose:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-nose.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-python-nose-1.2.1-6.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python33-python-pip
python33-python-pip:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-pip.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-python-pip-1.4.1-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python33-python-psycopg2
python33-python-psycopg2:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-psycopg2.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-python-psycopg2-2.4.5-10.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python33-python-pygments
python33-python-pygments:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-pygments.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-python-pygments-1.5-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python33-python-setuptools
python33-python-setuptools:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-setuptools.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-python-setuptools-0.6.28-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python33-python-simplejson
python33-python-simplejson:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-simplejson.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-python-simplejson-3.0.5-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python33-python-sphinx
python33-python-sphinx:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-sphinx.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-python-sphinx-1.1.3-8.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python33-python-sqlalchemy
python33-python-sqlalchemy:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-sqlalchemy.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-python-sqlalchemy-0.7.9-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: python33-python-virtualenv
python33-python-virtualenv:
	mock $(PYTHON33_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/python33-virtualenv.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(PYTHON33_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/python33-python-virtualenv-1.10.1-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Ruby 1.9.3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


.PHONY: ruby193-all
ruby193-all: ruby193 ruby193-libyaml ruby193-ruby ruby193-v8
ruby193-gems-all: \
	ruby193-rubygem-arel \
	ruby193-rubygem-bacon \
	ruby193-rubygem-builder \
	ruby193-rubygem-bundler \
	ruby193-rubygem-coffee-script \
	ruby193-rubygem-coffee-script-source \
	ruby193-rubygem-diff-lcs \
	ruby193-rubygem-erubis \
	ruby193-rubygem-execjs \
	ruby193-rubygem-hike \
	ruby193-rubygem-http_connection \
	ruby193-rubygem-journey \
	ruby193-rubygem-jquery-rails \
	ruby193-rubygem-metaclass \
	ruby193-rubygem-mime-types \
	ruby193-rubygem-net-http-persistent \
	ruby193-rubygem-polyglot \
	ruby193-rubygem-rack \
	ruby193-rubygem-rack-cache \
	ruby193-rubygem-rails \
	ruby193-rubygem-railties \
	ruby193-rubygem-ref \
	ruby193-rubygem-rspec \
	ruby193-rubygem-sass \
	ruby193-rubygem-sqlite3 \
	ruby193-rubygem-test_declarative \
	ruby193-rubygem-tilt \
	ruby193-rubygem-treetop \
	ruby193-rubygem-tzinfo \
	ruby193-rubygem-ZenTest \
	ruby193-rubygem-introspection \
	ruby193-rubygem-sass-rails \
	ruby193-rubygem-rspec-core \
	ruby193-rubygem-mocha \
	ruby193-rubygem-fakeweb \
	ruby193-rubygem-rspec-expectations \
	ruby193-rubygem-rspec-mocks \
	ruby193-rubygem-rcov \
	ruby193-rubygem-i18n \
	ruby193-rubygem-multi_json \
	ruby193-rubygem-therubyracer \
	ruby193-rubygem-mail \
	ruby193-rubygem-bcrypt-ruby \
	ruby193-rubygem-thor \
	ruby193-rubygem-sprockets \
	ruby193-rubygem-uglifier \
	ruby193-rubygem-activesupport \
	ruby193-rubygem-activemodel \
	ruby193-rubygem-activerecord \
	ruby193-rubygem-activeresource \
	ruby193-rubygem-sinatra \
	ruby193-rubygem-rack-test \
	ruby193-rubygem-rack-ssl \
	ruby193-rubygem-rack-protection \
	ruby193-rubygem-actionpack \
	ruby193-rubygem-actionmailer \
	ruby193-rubygem-coffee-rails

### ^^^ I have been able to build down to thor, without hitting a wall for now  I
### am moving to node and others and will come back to ruby issues.
###



.PHONY: ruby193
ruby193:
	mock $(SCL_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/ruby193.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(SCL_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-1-11.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-libyaml
ruby193-libyaml:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/libyaml.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-libyaml-0.1.4-5.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-ruby
ruby193-ruby:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/ruby.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-ruby-1.9.3.448-38.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-v8
ruby193-v8:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/v8.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-v8-3.14.5.10-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

.PHONY: ruby193-rubygem-actionmailer
ruby193-rubygem-actionmailer:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-actionmailer.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-actionmailer-3.2.8-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-actionpack
ruby193-rubygem-actionpack:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-actionpack.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-actionpack-3.2.8-5.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-activemodel
ruby193-rubygem-activemodel:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-activemodel.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-activemodel-3.2.8-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-activerecord
ruby193-rubygem-activerecord:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-activerecord.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-activerecord-3.2.8-8.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-activeresource
ruby193-rubygem-activeresource:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-activeresource.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-activeresource-3.2.8-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-activesupport
ruby193-rubygem-activesupport:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-activesupport.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-activesupport-3.2.8-4.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-arel
ruby193-rubygem-arel:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-arel.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-arel-3.0.2-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-bacon
ruby193-rubygem-bacon:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-bacon.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-bacon-1.1.0-8.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-bcrypt-ruby
ruby193-rubygem-bcrypt-ruby:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-bcrypt-ruby.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-bcrypt-ruby-3.0.1-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-builder
ruby193-rubygem-builder:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-builder.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-builder-3.0.0-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-bundler
ruby193-rubygem-bundler:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-bundler.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-bundler-1.1.4-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-coffee-rails
ruby193-rubygem-coffee-rails:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-coffee-rails.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-coffee-rails-3.2.2-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-coffee-script
ruby193-rubygem-coffee-script:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-coffee-script.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-coffee-script-2.2.0-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-coffee-script-source
ruby193-rubygem-coffee-script-source:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-coffee-script-source.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-coffee-script-source-1.3.3-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-diff-lcs
ruby193-rubygem-diff-lcs:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-diff-lcs.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-diff-lcs-1.1.3-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-erubis
ruby193-rubygem-erubis:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-erubis.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-erubis-2.7.0-4.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-execjs
ruby193-rubygem-execjs:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-execjs.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-execjs-1.4.0-4.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-fakeweb
ruby193-rubygem-fakeweb:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-fakeweb.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-fakeweb-1.3.0-8.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-hike
ruby193-rubygem-hike:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-hike.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-hike-1.2.1-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-http_connection
ruby193-rubygem-http_connection:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-http_connection.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-http_connection-1.4.1-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-i18n
ruby193-rubygem-i18n:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-i18n.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-i18n-0.6.0-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-introspection
ruby193-rubygem-introspection:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-introspection.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-introspection-0.0.2-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-journey
ruby193-rubygem-journey:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-journey.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-journey-1.0.4-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-jquery-rails
ruby193-rubygem-jquery-rails:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-jquery-rails.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-jquery-rails-2.0.2-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-mail
ruby193-rubygem-mail:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-mail.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-mail-2.4.4-4.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-metaclass
ruby193-rubygem-metaclass:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-metaclass.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-metaclass-0.0.1-8.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-mime-types
ruby193-rubygem-mime-types:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-mime-types.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-mime-types-1.19-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-mocha
ruby193-rubygem-mocha:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-mocha.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-mocha-0.12.10-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-multi_json
ruby193-rubygem-multi_json:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-multi_json.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-multi_json-1.3.6-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-net-http-persistent
ruby193-rubygem-net-http-persistent:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-net-http-persistent.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-net-http-persistent-2.7-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-polyglot
ruby193-rubygem-polyglot:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-polyglot.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-polyglot-0.3.3-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-rack
ruby193-rubygem-rack:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-rack.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-rack-1.4.1-5.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-rack-cache
ruby193-rubygem-rack-cache:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-rack-cache.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-rack-cache-1.2-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-rack-protection
ruby193-rubygem-rack-protection:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-rack-protection.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-rack-protection-1.2.0-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-rack-ssl
ruby193-rubygem-rack-ssl:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-rack-ssl.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-rack-ssl-1.3.2-7.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-rack-test
ruby193-rubygem-rack-test:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-rack-test.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-rack-test-0.6.1-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-rails
ruby193-rubygem-rails:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-rails.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-rails-3.2.8-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-railties
ruby193-rubygem-railties:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-railties.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-railties-3.2.8-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-rcov
ruby193-rubygem-rcov:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-rcov.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-rcov-0.9.9-9.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-ref
ruby193-rubygem-ref:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-ref.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-ref-1.0.0-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-rspec
ruby193-rubygem-rspec:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-rspec.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-rspec-2.11.0-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-rspec-core
ruby193-rubygem-rspec-core:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-rspec-core.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-rspec-core-2.11.1-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-rspec-expectations
ruby193-rubygem-rspec-expectations:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-rspec-expectations.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-rspec-expectations-2.11.1-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-rspec-mocks
ruby193-rubygem-rspec-mocks:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-rspec-mocks.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-rspec-mocks-2.11.1-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-sass
ruby193-rubygem-sass:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-sass.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-sass-3.1.20-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-sass-rails
ruby193-rubygem-sass-rails:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-sass-rails.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-sass-rails-3.2.5-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-sinatra
ruby193-rubygem-sinatra:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-sinatra.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-sinatra-1.3.2-12.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-sprockets
ruby193-rubygem-sprockets:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-sprockets.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-sprockets-2.4.5-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-sqlite3
ruby193-rubygem-sqlite3:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-sqlite3.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-sqlite3-1.3.6-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-test_declarative
ruby193-rubygem-test_declarative:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-test_declarative.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-test_declarative-0.0.5-3.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-therubyracer
ruby193-rubygem-therubyracer:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-therubyracer.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-therubyracer-0.11.0-0.6.beta5.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-thor
ruby193-rubygem-thor:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-thor.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-thor-0.15.4-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-tilt
ruby193-rubygem-tilt:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-tilt.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-tilt-1.3.3-10.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-treetop
ruby193-rubygem-treetop:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-treetop.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-treetop-1.4.10-6.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-tzinfo
ruby193-rubygem-tzinfo:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-tzinfo.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-tzinfo-0.3.33-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-uglifier
ruby193-rubygem-uglifier:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-uglifier.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-uglifier-1.2.6-2.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

.PHONY: ruby193-rubygem-ZenTest
ruby193-rubygem-ZenTest:
	mock $(RUBY193_OPTIONS) --buildsrpm --spec=$(ROOT)/SPECS/rubygem-ZenTest.spec --sources $(ROOT)/SOURCES --resultdir=$(ROOT)/SRPMS
	mock $(RUBY193_OPTIONS) --rebuild --resultdir=$(ROOT)/RPMS $(ROOT)/SRPMS/ruby193-rubygem-ZenTest-4.8.1-1.el$(EPEL_VERSION).src.rpm
	make EPEL_VERSION=$(EPEL_VERSION) createrepo

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
