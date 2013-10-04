%{?scl:%scl_package nodejs-rimraf}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-rimraf
Version:    2.1.4
Release:    2%{?dist}
Summary:    A deep deletion module for node.js
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/rimraf
Source0:    http://registry.npmjs.org/rimraf/-/rimraf-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%summary (like `rm -rf`).

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/rimraf
cp -pr rimraf.js package.json %{buildroot}%{nodejs_sitelib}/rimraf

%nodejs_symlink_deps

%check
%{?scl:scl enable %scl "}
cd test
bash run.sh
%{?scl:"}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/rimraf
%doc AUTHORS LICENSE README.md

%changelog
* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1.4-2
- Add support for software collections

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.4-1
- new upstream release 2.1.4

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-1
- new upstream release 2.1.1
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.1-2
- guard Requires for F17 automatic depedency generation

* Thu Feb 09 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.1-1
- new upstream release 2.0.1

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.9-1
- new upstream release

* Tue Aug 23 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.3-1
- initial package
