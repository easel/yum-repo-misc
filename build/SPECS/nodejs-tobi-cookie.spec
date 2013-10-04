%{?scl:%scl_package nodejs-tobi-cookie}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:           %{?scl_prefix}nodejs-tobi-cookie
Epoch:          1
Version:        0.2.0
Release:        2%{?dist}
Summary:        A cookie handling and cookie jar library for Node.js
BuildArch:      noarch

Group:          System Environment/Libraries
#ASL 2.0 added upstream
#https://github.com/mikeal/cookie-jar/blob/master/LICENSE
License:        ASL 2.0
URL:            https://github.com/mikeal/cookie-jar
Source0:        http://registry.npmjs.org/cookie-jar/-/cookie-jar-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

#this needs to get renamed to nodejs-cookie-jar soon
Provides:       %{?scl_prefix}nodejs-cookie-jar = %{version}

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%summary.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/cookie-jar
cp -p index.js jar.js package.json %{buildroot}%{nodejs_sitelib}/cookie-jar

%nodejs_symlink_deps

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/cookie-jar

%changelog
* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:0.2.0-2
- Add support for software collections

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.2.1-1
- now unbundled from tobi, called cookie-jar upstream

* Sat Jan 26 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.2-2
- add missing build section

* Tue Jan 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.2-1
- initial package