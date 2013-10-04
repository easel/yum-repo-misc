%global scl php54
%if 0%{?scl_package:1}
%scl_package %scl
%else
%global scl_name %{scl}
%endif

Summary:       Package that installs %scl
Name:          %scl_name
Version:       1
Release:       7%{?dist}
Group:         Development/Languages
License:       GPLv2+

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: scl-utils-build
# Temporary work-around
BuildRequires: iso-codes

Requires:      %{?scl_prefix}php-common
Requires:      %{?scl_prefix}php-cli
Requires:      %{?scl_prefix}php-pear

%description
This is the main package for %scl Software Collection.

%package runtime
Summary:   Package that handles %scl Software Collection.
Group:     Development/Languages
Requires:  scl-utils

%description runtime
Package shipping essential scripts to work with %scl Software Collection.

%package build
Summary:   Package shipping basic build configuration
Group:     Development/Languages
Requires:  scl-utils-build

%description build
Package shipping essential configuration macros to build %scl Software Collection.


%prep
%setup -c -T

# Not required for now
#export LIBRARY_PATH=%{_libdir}\${LIBRARY_PATH:+:\${LIBRARY_PATH}}
#export LD_LIBRARY_PATH=%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}

cat <<EOF | tee enable
export PATH=%{_bindir}:%{_sbindir}\${PATH:+:\${PATH}}
export MANPATH=%{_mandir}:\${MANPATH}
EOF


%install
mkdir -p %{buildroot}%{_scl_scripts}/root
install -m 644 enable  %{buildroot}%{_scl_scripts}/enable

%scl_install


%files

%files runtime
%defattr(-,root,root)
%scl_files

%files build
%defattr(-,root,root)
%{_root_sysconfdir}/rpm/macros.%{scl}-config


%changelog
* Fri May 23 2013 Remi Collet <rcollet@redhat.com> 1-7
- Really fix MANPATH variable definition (#966390)

* Thu May 23 2013 Remi Collet <rcollet@redhat.com> 1-6
- Fix MANPATH variable definition (#966390)

* Fri May  3 2013 Remi Collet <rcollet@redhat.com> 1-5
- Fix PATH variable definition (#957204)
- meta package requires php-cli and php-pear

* Mon Apr 29 2013 Remi Collet <rcollet@redhat.com> 1-4
- Fix LIBRARY_PATH variabls definition (#957204)

* Wed Apr 10 2013 Remi Collet <rcollet@redhat.com> 1-3
- drop unneeded LD_LIBRARY_PATH

* Tue Oct 23 2012 Remi Collet <rcollet@redhat.com> 1-2
- EL-5 compatibility (buildroot, ...)

* Fri Sep 28 2012 Remi Collet <rcollet@redhat.com> 1-1
- initial packaging

