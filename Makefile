DISTROS=epel/5
ARCHES=SRPMS x86_64 i386

default: createrepo

.PHONY: createrepo
createrepo:
	for distro in $(DISTROS); do \
		for arch in $(ARCHES); do \
			cd $$distro/$$arch && createrepo .; \
		done; \
	done
