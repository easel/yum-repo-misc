%{?scl:%scl_package nodejs-slide}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-slide
Version:    1.1.3
Release:    6%{?dist}
Summary:    A flow control library that fits in a slideshow
# license present in source control, will be added to future release
# https://raw.github.com/isaacs/slide-flow-control/master/LICENSE
License:    MIT
URL:        https://github.com/isaacs/slide-flow-control
Source0:    http://registry.npmjs.org/slide/-/slide-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Provides simple, easy callbacks for node.js.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/slide
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/slide

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/slide
%doc README.md nodejs-controlling-flow.pdf

%changelog
* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1.3-6
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-4
- add missing build section
- mention missing license

* Thu Apr 26 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-3
- missing package.json

* Thu Apr 26 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-2
- bring into conformance with newer library packaging standards
- guard Requires for F17 automatic dependency generation

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-1
- initial package