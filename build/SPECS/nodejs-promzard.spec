%{?scl:%scl_package nodejs-promzard}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:           %{?scl_prefix}nodejs-promzard
Version:        0.2.0
Release:        5%{?dist}
Summary:        A prompting wizard for building files from specialized PromZard modules
BuildArch:      noarch

Group:          System Environment/Libraries
# license will be included in next upstream release
# # https://raw.github.com/isaacs/promzard/master/LICENSE
License:        BSD
URL:            https://github.com/isaacs/promzard
Source0:        http://registry.npmjs.org/promzard/-/promzard-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
A prompting wizard for building files from specialized PromZard modules.

The goal is a nice drop-in enhancement for `npm init`.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{nodejs_sitelib}/promzard
cp -pr package.json promzard.js %{buildroot}%{nodejs_sitelib}/promzard

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/promzard
%doc example README.md

%changelog
* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.2.0-5
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-2
- fix summary, description, license

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- initial package generated by npm2rpm