
%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

%{?scl:%scl_package nodejs-sigmund}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}nodejs-sigmund
Version:        1.0.0
Release:        4%{?dist}
Summary:        Quick and dirty signatures for Objects
BuildArch:      noarch

Group:          System Environment/Libraries
License:        BSD
URL:            https://github.com/isaacs/sigmund
Source0:        http://registry.npmjs.org/sigmund/-/sigmund-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Quick and dirty signatures for Objects.

This is like a much faster `deepEquals` comparison, which returns a
string key suitable for caches and the like.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{nodejs_sitelib}/sigmund
cp -pr package.json sigmund.js %{buildroot}%{nodejs_sitelib}/sigmund

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/sigmund
%doc LICENSE README.md bench.js

%changelog
* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.0-4
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-1
- initial package generated by npm2rpm