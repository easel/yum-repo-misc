#!/bin/bash
DISTROS=/vagrant/epel/5 /vagrant/epel/6
ARCHES=SRPMS x86_64 i386

default: default

.PHONY: default
default: 
	echo "pick a target"

.PHONY: move 
move: move checkin use-master

.PHONY: build
build: createrepo checkin use-master


.PHONY: use-gh-pages
use-gh-pages:
	git checkout gh-pages

.PHONY: move
move: use-gh-pages
	mv build/RPMS/*el5*x86_64.rpm epel/5/x86_64/
	mv build/RPMS/*el5*src.rpm epel/5/SRPMS/
	mv build/RPMS/*el6*x86_64.rpm epel/6/x86_64/
	mv build/RPMS/*el6*src.rpm epel/6/SRPMS/


.PHONY: createrepo
createrepo: use-gh-pages
	for distro in $(DISTROS); do \
		for arch in $(ARCHES); do \
			vagrant ssh --command "cd $$distro/$$arch && createrepo -s sha ."; \
		done; \
	done

.PHONY: checkin
cheeckin:
	git add -u epel
	git add epel
	git commit -m 'updating repository versions'

.PHONY: use-master
use-master:
	git checkout master
