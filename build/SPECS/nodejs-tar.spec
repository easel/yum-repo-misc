%{?scl:%scl_package nodejs-tar}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-tar
Version:    0.1.17
Release:    2%{?dist}
Summary:    Tar for Node.js
License:    BSD
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/node-tar
Source0:    http://registry.npmjs.org/tar/-/tar-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
A Node.js module that supports reading and writing POSIX "tar" archives.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/tar
cp -pr lib tar.js package.json %{buildroot}%{nodejs_sitelib}/tar

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/tar
%doc README.md examples LICENCE

%changelog
* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.17-2
- Add support for software collections

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.17-1
- new upstream release 0.1.17

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.16-1
- new upstream release 0.1.16

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.14-3
- add missing build section
- fix URL

* Sun Jan 06 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.14-2
- provide a better description and summary

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.14-1
- new upstream release 0.1.14
- clean up for submission

* Thu Mar 15 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.13-1
- new upstream release 0.1.13

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.12-1
- initial package