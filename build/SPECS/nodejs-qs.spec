%{?scl:%scl_package nodejs-qs}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

%global enable_tests 0

Name:       %{?scl_prefix}nodejs-qs
Version:    0.5.6
Release:    2%{?dist}
Summary:    Query string parser for Node.js
# License text is included in Readme.md
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/visionmedia/node-querystring
Source0:    http://registry.npmjs.org/qs/-/qs-%{version}.tgz
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  npm(expect.js)
BuildRequires:  npm(growl)
BuildRequires:  npm(jade)
BuildRequires:  npm(mocha)
BuildRequires:  npm(querystring)
%endif

%description
This is a query string parser for node and the browser supporting nesting,
as it was removed from 0.3.x, so this library provides the previous and
commonly desired behavior (and twice as fast). Used by express, connect
and others.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/qs
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/qs

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
cp -pr %{nodejs_sitelib} .
%{nodejs_sitelib}/mocha/bin/mocha --ui bdd
%endif

%files
%doc History.md Readme.md examples.js
%{nodejs_sitelib}/qs

%changelog
* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.5.6-2
- Add support for software collections

* Wed Apr 10 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.6-1
- update to upstream release 0.5.6

* Fri Mar 22 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.5-1
- update to upstream release 0.5.5

* Sat Mar 16 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.4-1
- update to upstream release 0.5.4

* Wed Feb 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.3-3
- fix typo in %%description

* Wed Feb 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.3-2
- fix typo in %%summary

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.3-1
- initial package