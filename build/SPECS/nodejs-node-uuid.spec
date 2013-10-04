%{?scl:%scl_package nodejs-node-uuid}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

%global enable_tests 1

Name:       %{?scl_prefix}nodejs-node-uuid
Version:    1.4.0
Release:    3%{?dist}
Summary:    Simple and fast generation of RFC4122 (v1 and v4) UUIDs for Node.js
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/broofa/node-uuid
Source0:    http://registry.npmjs.org/node-uuid/-/node-uuid-%{version}.tgz
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
This Node.js module provides simple and fast generation of RFC4122 (v1 and v4)
UUIDs. It runs in Node.js and all browsers and can also generate
cryptographically strong random numbers.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/node-uuid
cp -pr package.json uuid.js \
    %{buildroot}%{nodejs_sitelib}/node-uuid

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
%{?scl:scl enable %{scl} "}
ln -sf %{nodejs_sitelib} .
%__nodejs test/test.js
%{?scl:"}
%endif

%files
%doc LICENSE.md README.md
%{nodejs_sitelib}/node-uuid

%changelog
* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.0-3
- Add support for software collections

* Fri Apr 05 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.0-2
- do not include benchmark/ directory

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.0-1
- initial package
