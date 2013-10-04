%{?scl:%scl_package nodejs-glob}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-glob
Version:    3.1.21
Release:    2%{?dist}
Summary:    A little globber for Node.js
License:    BSD
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/node-glob
Source0:    http://registry.npmjs.org/glob/-/glob-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
This is a glob implementation in pure JavaScript. It uses the minimatch library
to do its matching.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/glob
cp -pr glob.js package.json %{buildroot}%{nodejs_sitelib}/glob

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/glob
%doc LICENSE README.md examples

%changelog
* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.1.21-2
- Add support for software collections

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.21-1
- new upstream release 3.1.21

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.20-1
- new upstream release 3.1.20

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.14-2
- add missing build section
- adjust summary/description slightly

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.14-1
- new upstream release 3.1.14
- clean up for submission

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.9-1
- new upstream release 3.1.9

* Fri Mar 16 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.6-1
- initial package