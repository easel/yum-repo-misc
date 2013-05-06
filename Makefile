#!/bin/bash
DISTROS=/vagrant/epel/5
ARCHES=SRPMS x86_64 i386

default: default

.PHONY: default
default: 
	echo "pick a target"

.PHONY: build
build: createrepo checkin use-master


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
			vagrant ssh --command "cd $$distro/$$arch && createrepo -s sha ."; \
		done; \
	done

.PHONY: checkin
checkin:
	git add -u epel
	git add epel
	git commit -m 'updating repository versions'

.PHONY: use-master
use-master:
	git checkout master
