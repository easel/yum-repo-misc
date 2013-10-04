%{?scl:%scl_package nodejs-fstream-npm}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-fstream-npm
Version:    0.1.4
Release:    2%{?dist}
Summary:    An fstream class for creating npm packages
License:    BSD
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/fstream-npm
Source0:    http://registry.npmjs.org/fstream-npm/-/fstream-npm-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%{summary}.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/fstream-npm
cp -pr fstream-npm.js package.json %{buildroot}%{nodejs_sitelib}/fstream-npm

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/fstream-npm
%doc README.md example LICENCE

%changelog
* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.4-2
- Add support for software collections

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.4-1
- new upstream release 0.1.4

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.3-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.3-1
- new upstream release 0.1.3
- clean up for submission

* Wed Apr 18 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-1
- New upstream release 0.0.6

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-1
- initial package