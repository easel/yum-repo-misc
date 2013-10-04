%{?scl:%scl_package nodejs-fstream}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-fstream
Version:    0.1.22
Release:    2%{?dist}
Summary:    Advanced file system stream objects for Node.js
License:    BSD
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/fstream
Source0:    http://registry.npmjs.org/fstream/-/fstream-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Provides advanced file system stream objects for Node.js.  These objects are
like FS streams, but with stat on them, and support directories and
symbolic links, as well as normal files.  Also, you can use them to set
the stats on a file, even if you don't change its contents, or to create
a symlink, etc.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/fstream
cp -pr lib fstream.js package.json %{buildroot}%{nodejs_sitelib}/fstream

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/fstream
%doc LICENSE README.md examples

%changelog
* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.22-2
- Add support for software collections

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.22-1
- new upstream release 0.1.22

* Sun Jan 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.21-3
- fix License tag

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.21-2
- add missing build section
- fix summary/description

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.21-1
- new upstream release 0.1.21
- clean up for submission

* Thu Mar 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.18-1
- New upstream release 0.1.18

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.17-1
- new upstream release 0.1.17

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.14-1
- new upstream release 0.1.14

* Sun Mar 04 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.13-1
- new upstream release 0.1.13

* Thu Feb 09 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.12-1
- new upstream release 0.1.12

* Sat Jan 21 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.11-1
- initial package