%{?scl:%scl_package nodejs-boom}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-boom
Version:    0.4.0
Release:    2%{?dist}
Summary:    HTTP friendly error objects
License:    BSD
Group:      Development/Libraries
URL:        https://github.com/spumko/boom
Source0:    http://registry.npmjs.org/boom/-/boom-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
This library provides friendly JavaScript objects that represent HTTP errors.

%prep
%setup -q -n package

#fix perms
chmod 0644 README.md LICENSE images/* lib/* index.js package.json

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/boom
cp -pr lib index.js package.json %{buildroot}%{nodejs_sitelib}/boom

%nodejs_symlink_deps

#Yet Another Unpackaged Test Framework (lab)
#%%check
#make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/boom
%doc README.md LICENSE images

%changelog
* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.4.0-2
- Add support for software collections

* Mon Apr 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.0-1
- initial package