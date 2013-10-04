%global scl python27
%scl_package %scl
%global _turn_off_bytecompile 1

%global install_scl 1

Summary: Package that installs %scl
Name: %scl_name
Version: 1
Release: 10%{?dist}
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
* Mon May 27 2013 Matej Stuchlik <mstuchli@redhat.com> - 1-10
- BZ966391: Another MANPATH fix.

* Thu May 23 2013 Matej Stuchlik <mstuchli@redhat.com> - 1-9
- BZ966391: MANPATH fix

* Tue May 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1-8
- Add dependency on python-sphinx and python-nose to draw in
all the useful dependencies from the collection.

* Tue Apr 30 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1-7
- Define variables in scriptlets in a really secure way (RHBZ#957208).
- Correct the sed on macros file to substitute all occurences on one line.

* Wed Apr 24 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1-6
- Utilize the new package_override function to override __os_install_post.
- Move scripts to python-devel, so that it can be utilized in other
collections, that won't BR this metapackage.

* Wed Apr 24 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1-5
- Delete the __os_install_post redefinition in favor of new definition
in scl-utils-build.

* Wed Apr 10 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1-4
- Define variables in enable scriptlets in a secure way (RHBZ #949000).

* Mon Dec 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1-3
- Rebuilt for PPC.

* Wed Oct 10 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1-2
- Enable installing the whole SCL.

* Fri Sep 14 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1-1
- Initial package.
