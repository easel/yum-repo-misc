%{?scl:%scl_package nodejs-hawk}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-hawk
Version:    0.12.1
Release:    3%{?dist}
Summary:    HTTP Hawk authentication scheme
License:    BSD
Group:      Development/Libraries
URL:        https://github.com/hueniverse/hawk
Source0:    http://registry.npmjs.org/hawk/-/hawk-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

Patch1: Deminified-crypto-functions.patch 
%description
Hawk is an HTTP authentication scheme using a message authentication code (MAC)
algorithm to provide partial HTTP request cryptographic verification.

%prep
%setup -q -n package
%patch1 -p1
#fix perms
chmod 0644 README.md LICENSE example/* images/* lib/* index.js package.json

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/hawk
cp -pr lib index.js package.json %{buildroot}%{nodejs_sitelib}/hawk

%nodejs_symlink_deps

#Yet Another Unpackaged Test Framework (lab)
#%%check
#make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/hawk
%doc README.md LICENSE example images

%changelog
* Fri Aug 09 2013 Tomas Hrcka <thrcka@redhat.com> - 0.12.1-3
- added patch to deminify implemented crypto functions

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.12.1-2
- Add support for software collections

* Tue Apr 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.12.1-1
- new upstream release 0.12.1

* Mon Apr 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.11.1-2
- fix rpmlint warnings

* Fri Apr 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.11.1-1
- initial package
