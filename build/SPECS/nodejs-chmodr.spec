%{?scl:%scl_package nodejs-chmodr}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-chmodr
Version:    0.1.0
Release:    3%{?dist}
Summary:    Recursively change UNIX file permissions
License:    BSD
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/chmodr
Source0:    http://registry.npmjs.org/chmodr/-/chmodr-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%{summary}, like `chmod -R`.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/chmodr
cp -pr chmodr.js package.json %{buildroot}%{nodejs_sitelib}/chmodr

%nodejs_symlink_deps

# disabled; TAP is not in the distro yet
#%%check
#%%tap test/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/chmodr
%doc README.md LICENSE

%changelog
* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.0-3
- Add support for software collections

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.0-2
- fix License tag

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.0-1
- initial package