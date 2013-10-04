%{?scl:%scl_package nodejs-proto-list}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-proto-list
Version:    1.2.2
Release:    4%{?dist}
Summary:    A list of objects bound by prototype chain
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/proto-list
Source0:    http://registry.npmjs.org/proto-list/-/proto-list-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel
#BuildRequires:  nodejs-tap

%description
A list of objects bound by prototype chain.  Used for the Node.js package
manager (npm) configuration.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/proto-list
cp -p package.json proto-list.js %{buildroot}%{nodejs_sitelib}/proto-list

%nodejs_symlink_deps

# We currently don't run tests because I'd have to file another ten or
# so review reuqests for the node.js TAP testing framework and methinks there
# are enough of those for now.  ;-)
##%%check
##%%nodejs proto-list.js

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/proto-list
%doc LICENSE README.md

%changelog
* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.2-4
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.2-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.2-1
- new upstream release 1.2.2
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-4
- bring in line with newer module packaging standards

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-3
- guard Requires for F17 automatic depedency generation

* Sun Dec 18 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-2
- add Group to make EL5 happy

* Tue Aug 23 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-1
- initial package