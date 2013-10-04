%global scl nodejs010
%scl_package %scl
%global install_scl 1

Summary: %scl Software Collection
Name: %scl_name
Version: 1
Release: 17%{?dist}

Source1: macros.nodejs
Source2: nodejs.attr
Source3: nodejs.prov
Source4: nodejs.req
Source5: nodejs-symlink-deps
Source6: nodejs-fixdep
Source7: nodejs_native.attr

License: MIT

%if 0%{?install_scl}
Requires: %{scl_prefix}nodejs
Requires: %{scl_prefix}npm
Requires: %{scl_prefix}runtime
%endif

BuildRequires: scl-utils-build
BuildRequires: python-devel

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

%prep
%setup -c -T

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_scl_scripts}/root
cat >> %{buildroot}%{_scl_scripts}/enable << EOF
export PATH=%{_bindir}\${PATH:+:\${PATH}}
export LD_LIBRARY_PATH=%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}
export PYTHONPATH=%{_scl_root}%{python_sitelib}\${PYTHONPATH:+:\${PYTHONPATH}}
export MANPATH=%{_mandir}:\$MANPATH 
EOF

# install rpm magic
install -Dpm0644 %{SOURCE1} %{buildroot}%{_root_sysconfdir}/rpm/macros.%{name}
install -Dpm0644 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/fileattrs/%{name}.attr
install -pm0755 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/%{name}.prov
install -pm0755 %{SOURCE4} %{buildroot}%{_rpmconfigdir}/%{name}.req
install -pm0755 %{SOURCE5} %{buildroot}%{_rpmconfigdir}/%{name}-symlink-deps
install -pm0755 %{SOURCE6} %{buildroot}%{_rpmconfigdir}/%{name}-fixdep
install -Dpm0644 %{SOURCE7} %{buildroot}%{_rpmconfigdir}/fileattrs/%{name}_native.attr


# ensure Requires are added to every native module that match the Provides from
# the nodejs build in the buildroot
cat << EOF > %{buildroot}%{_rpmconfigdir}/%{name}_native.req
#!/bin/sh
echo 'nodejs010-nodejs(abi) = %nodejs_abi'
echo 'nodejs010-nodejs(v8-abi) = %v8_abi'
EOF
chmod 0755 %{buildroot}%{_rpmconfigdir}/%{name}_native.req

cat << EOF > %{buildroot}%{_rpmconfigdir}/%{name}-require.sh
#!/bin/sh
%{_rpmconfigdir}/%{name}.req $*
%{_rpmconfigdir}/find-requires $*
EOF
chmod 0755 %{buildroot}%{_rpmconfigdir}/%{name}-require.sh

cat << EOF > %{buildroot}%{_rpmconfigdir}/%{name}-provide.sh
#!/bin/sh
%{_rpmconfigdir}/%{name}.prov $*
%{_rpmconfigdir}/find-provides $*
EOF
chmod 0755 %{buildroot}%{_rpmconfigdir}/%{name}-provide.sh

%scl_install
# scl doesn't include this directory
mkdir -p %{buildroot}%{_scl_root}%{python_sitelib}
mkdir -p %{buildroot}%{_libdir}/pkgconfig

%files

%files runtime
%scl_files
%dir %{_scl_root}%{python_sitelib}
%dir %{_libdir}/pkgconfig

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config
%{_root_sysconfdir}/rpm/macros.%{name}
%{_rpmconfigdir}/fileattrs/%{name}*.attr
%{_rpmconfigdir}/%{name}*


%changelog
* Thu Aug 15 2013 thrcka@redhat.com - 1-17
- clean up after previous fix

* Fri Aug 09 2013 thrcka@redhat.com - 1-16
- RHBZ#993425 - nodejs010.req fails when !noarch 

* Mon Jun 03 2013 thrcka@redhat.com - 1-15
- Changed licence to MIT

* Thu May 23 2013 Tomas Hrcka <thrcka@redhat.com> - 1-14.1
- fixed typo in MANPATH

* Thu May 23 2013 Tomas Hrcka <thrcka@redhat.com> - 1-14
- Changed MAN_PATH so it does not ignore man pages from host system

* Thu May  9 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-13
- Remove colons forgotten in scriplets

* Tue May 07 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-12
- Add runtime dependency on scl-runtime

* Mon May 06 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-11
- Add pkgconfig file ownership

* Mon May 06 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-10
- Workaround scl-utils not generating all directory ownerships (#956213)

* Mon May 06 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-9
- Fix enable scriptlet evironment expansion (#956788)

* Wed Apr 17 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-8
- Extend MANPATH env variable
- Add npm to meta package requires

* Mon Apr 15 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-7
- Update macros and requires/provides generator to latest

* Wed Apr 10 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-6
- Fix rpm requires/provides generator paths
- Add requires to main meta package

* Mon Apr 08 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-5
- Make package architecture specific for libdir usage

* Mon Apr 08 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-4
- Add rpm macros and tooling

* Mon Apr 08 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-3
- Add proper scl-utils-build requires

* Fri Apr 05 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-2
- Add PYTHONPATH to configuration

* Tue Mar 26 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-1
- Initial version of the Node.js Software Collection
