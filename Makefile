#!/bin/bash
DISTROS=epel/5
ARCHES=SRPMS x86_64 i386

default: default

.PHONY: default
default: use-gh-pages move createrepo use-master

.PHONY: use-gh-pages
use-gh-pages:
	git checkout gh-pages

.PHONY: move
move:
	mv build/RPMS/*el5*x86_64.rpm epel/5/x86_64/
	mv build/RPMS/*el5*src.rpm epel/5/SRPMS/

.PHONY: createrepo
createrepo:
	for distro in $(DISTROS); do \
		for arch in $(ARCHES); do \
			pushd . && cd $$distro/$$arch && createrepo -s sha . && popd; \
		done; \
	done

.PHONY: use-master
use-master:
	git checkout master
