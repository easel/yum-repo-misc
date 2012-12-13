#!/bin/bash
DISTROS=5
ARCHES=SRPMS x86_64 i386

default: createrepo

.PHONY: createrepo
createrepo:
	for distro in $(DISTROS); do \
		for arch in $(ARCHES); do \
			pushd . && cd $$distro/$$arch && createrepo -s sha . && popd; \
		done; \
	done
