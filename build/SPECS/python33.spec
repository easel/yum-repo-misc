%global scl python33
## General notes about python33 SCL packaging
# - the names of packages are NOT prefixed with 'python3-' (e.g. are the same as in Fedora)
# - the names of binaries of Python 3 itself are both python{-debug,...} and python3{-debug,...}
# so both are usable in shebangs, the non-versioned binaries are preferred.
# - the names of other binaries are NOT prefixed with 'python3-'.
# - the macros are left with the '3' inside, so there is no %{__python},
# you must use %{__python3} etc... This is done because we don't want to override the default
# %{__python} etc. macros in buildroot, if someone installs python33-build.

%scl_package %scl
%global _turn_off_bytecompile 1

%global install_scl 1

Summary: Package that installs %scl
Name: %scl_name
Version: 1
Release: 6%{?dist}
License: GPLv2+
Source0: macros.additional.%{scl}
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=857354
BuildRequires: iso-codes
BuildRequires: scl-utils-build
%if 0%{?install_scl}
Requires: %{scl_prefix}python
Requires: %{scl_prefix}python-jinja2
Requires: %{scl_prefix}python-nose
Requires: %{scl_prefix}python-simplejson
Requires: %{scl_prefix}python-setuptools
Requires: %{scl_prefix}python-sphinx
Requires: %{scl_prefix}python-sqlalchemy
Requires: %{scl_prefix}python-virtualenv
%endif

%description
This is the main package for %scl Software Collection.

%package runtime
Summary: Package that handles %scl Software Collection.
Requires: scl-utils

%description runtime
Package shipping essential scripts to work with %scl Software Collection.

%package build
Summary: Package shipping basic build configuration
Requires: scl-utils-build

%description build
Package shipping essential configuration macros to build %scl Software Collection.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_scl_scripts}/root
mkdir -p %{buildroot}%{_root_prefix}/lib/rpm/redhat
cat >> %{buildroot}%{_scl_scripts}/enable << EOF
export PATH=%{_bindir}\${PATH:+:\${PATH}}
export LD_LIBRARY_PATH=%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}
export MANPATH=%{_mandir}:\${MANPATH}
# For systemtap
export XDG_DATA_DIRS=%{_datadir}\${XDG_DATA_DIRS:+:\${XDG_DATA_DIRS}}
# For pkg-config
export PKG_CONFIG_PATH=%{_libdir}/pkgconfig\${PKG_CONFIG_PATH:+:\${PKG_CONFIG_PATH}}
EOF
%scl_install

# Add the aditional macros to macros.%%{scl}-config
cat %{SOURCE0} >> %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl}-config
sed -i 's|@scl@|%{scl}|g' %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl}-config

%files

%files runtime
%scl_files

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%changelog
* Mon May 27 2013 Robert Kuska <rkuska@redhat.com> - 1-6
- Another fix of MANPATH (RHBZ #966393)

* Thu May 23 2013 Robert Kuska <rkuska@redhat.com> - 1-5
- Fix MANPATH (RHBZ #966393).

* Tue May 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1-4
- Remove unneded rhel-5 specifics.
- Add some more dependencies to metapackage spec.
- Fix the enable scriptlet variable definition to be really secure.
- Move the rpm scripts to python-devel, so that possible depending
collections can use them as well.

* Thu Apr 11 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1-3
- Define variables in enable scriptlets in a secure way (RHBZ #949000).

* Thu Jan 31 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1-2
- Require the whole SCL on installation.

* Fri Dec 21 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1-1
- Initial package.
