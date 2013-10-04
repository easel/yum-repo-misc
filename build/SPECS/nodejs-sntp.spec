%{?scl:%scl_package nodejs-sntp}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-sntp
Version:    0.2.1
Release:    2%{?dist}
Summary:    SNTP v4 client (RFC4330) for Node.js
License:    BSD
Group:      Development/Libraries
URL:        https://github.com/hueniverse/sntp
Source0:    http://registry.npmjs.org/sntp/-/sntp-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
An SNTP v4 client (RFC4330) for Node.js. Simply connects to the NTP or SNTP
server requested and returns the server time along with the round-trip duration
and clock offset. To adjust the local time to the NTP time, add the returned 
time offset to the local time.

%prep
%setup -q -n package

#drop exec bit from everything
chmod 0644 *.js* README.md LICENSE examples/* lib/*

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/sntp
cp -pr lib index.js package.json %{buildroot}%{nodejs_sitelib}/sntp

%nodejs_symlink_deps

#Yet Another Unpackaged Test Framework (lab)
#%%check
#make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/sntp
%doc README.md LICENSE examples

%changelog
* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.2.1-2
- Add support for software collections

* Tue Apr 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.1-1
- new upstream release 0.2.1

* Mon Apr 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-2
- fix rpmlint warnings

* Fri Apr 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- initial package