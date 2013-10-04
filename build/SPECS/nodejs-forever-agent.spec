%{?scl:%scl_package nodejs-forever-agent}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-forever-agent
Version:    0.2.0
Release:    2%{?dist}
Summary:    HTTP Agent that keeps socket connections alive between keep-alive requests
# Apache 2.0 License added upstream, will appear in next release
# https://github.com/mikeal/forever-agent/blob/master/LICENSE
License:    ASL 2.0
Group:      Development/Libraries
URL:        https://github.com/mikeal/forever-agent
Source0:    http://registry.npmjs.org/forever-agent/-/forever-agent-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%{summary}.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/forever-agent
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/forever-agent

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/forever-agent

%changelog
* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.2.0-2
- Add support for software collections

* Fri Apr 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- initial package