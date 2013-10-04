%{?scl:%scl_package nodejs-nopt}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}


Name:       %{?scl_prefix}nodejs-nopt
Version:    2.1.1
Release:    2%{?dist}
Summary:    Node.js option parsing
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/nopt
Source0:    http://registry.npmjs.org/nopt/-/nopt-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
An option parsing library for Node.js and its package manager (npm).

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/nopt
cp -pr bin lib package.json %{buildroot}%{nodejs_sitelib}/nopt

mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/nopt/bin/nopt.js %{buildroot}%{_bindir}/nopt

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/nopt
%{_bindir}/nopt
%doc README.md LICENSE examples

%changelog
* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1.1-2
- Add support for software collections

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-1
- new upstream release 2.1.1

* Sun Jan 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.0-3
- fix symlink to nopt script

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.0-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.0-1
- new upstream release 2.0.0
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.10-4
- bring in line with newer module packaging standards

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.10-3
- guard Requires for F17 automatic depedency generation

* Sun Dec 18 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.10-2
- add Group to make EL5 happy

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> 1.0.10-1
- new upstream release

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.6-1
- initial package