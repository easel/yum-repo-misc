%global scl python27
%scl_package %scl
%global _turn_off_bytecompile 1

%global install_scl 1

Summary: Package that installs %scl
Name: %scl_name
Version: 1
Release: 3%{?dist}
License: GPLv2+
Source0: macros.additional.%{scl}
Source1: brp-python-bytecompile-with-scl-python
Source2: pythondeps-scl.sh
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=857354
BuildRequires: iso-codes
BuildRequires: scl-utils-build
%if 0%{?install_scl}
Requires: %{scl_prefix}python
Requires: %{scl_prefix}python-jinja2
Requires: %{scl_prefix}python-simplejson
Requires: %{scl_prefix}python-setuptools
Requires: %{scl_prefix}python-sqlalchemy
Requires: %{scl_prefix}python-virtualenv
Requires: %{scl_prefix}python-werkzeug
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
export PATH=%{_bindir}:\$PATH
export LD_LIBRARY_PATH=%{_libdir}:\$LD_LIBRARY_PATH
export MANPATH=%{_mandir}:\$MANPATH
# For systemtap
export XDG_DATA_DIRS=%{_datadir}:\$XDG_DATA_DIRS
# For pkg-config
export PKG_CONFIG_PATH=%{_libdir}/pkgconfig:\$PKG_CONFIG_PATH
EOF
%scl_install

# Add the aditional macros to macros.%%{scl}-config
cat %{SOURCE0} >> %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl}-config
# Copy the bytecompiling script into place
install -m 755 %{SOURCE1} %{buildroot}%{_root_prefix}/lib/rpm/redhat
install -m 755 %{SOURCE2} %{buildroot}%{_root_prefix}/lib/rpm

%files

%files runtime
%scl_files

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config
%{_root_prefix}/lib/rpm/redhat/brp-python-bytecompile-with-scl-python
%{_root_prefix}/lib/rpm/pythondeps-scl.sh

%changelog
* Mon Dec 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1-3
- Rebuilt for PPC.

* Wed Oct 10 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1-2
- Enable installing the whole SCL.

* Fri Sep 14 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1-1
- Initial package.
