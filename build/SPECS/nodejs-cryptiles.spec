%{?scl:%scl_package nodejs-cryptiles}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-cryptiles
Version:    0.2.0
Release:    2%{?dist}
Summary:    General purpose cryptography utilities for Node.js
License:    BSD
Group:      Development/Libraries
URL:        https://github.com/hueniverse/cryptiles
Source0:    http://registry.npmjs.org/cryptiles/-/cryptiles-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%{summary}.

%prep
%setup -q -n package

#fix perms
chmod 0644 README.md LICENSE lib/* index.js package.json

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/cryptiles
cp -pr lib index.js package.json %{buildroot}%{nodejs_sitelib}/cryptiles

%nodejs_symlink_deps

#Yet Another Unpackaged Test Framework (lab)
#%%check
#make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/cryptiles
%doc README.md LICENSE

%changelog
* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.2.0-2
- Add support for software collections

* Mon Apr 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- initial package