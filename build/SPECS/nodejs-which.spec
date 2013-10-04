%{?scl:%scl_package nodejs-which}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}


Name:       %{?scl_prefix}nodejs-which
Version:    1.0.5
Release:    7%{?dist}
Summary:    A JavaScript implementation of the 'which' command
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/node-which
Source0:    http://registry.npmjs.org/which/-/which-%{version}.tgz
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

mkdir -p %{buildroot}%{nodejs_sitelib}/which
cp -pr bin which.js package.json %{buildroot}%{nodejs_sitelib}/which

mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/which/bin/which %{buildroot}%{_bindir}/which-nodejs

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/which
%{_bindir}/which-nodejs
%doc README.md LICENSE

%changelog
* Fri May  3 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.5-7
- Fix broken symlink in bindir

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-6
- add macro for EPEL6 dependency generation

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.5-6
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-4
- fix symlink to executable
- actually install the executable!
- rename executable to which-nodejs

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-3
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-2
- Clean up for submission

* Sun Mar 04 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-1
- new upstream release 1.0.5

* Thu Feb 10 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.3-1
- new upstream release 1.0.3

* Sun Dec 18 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-2
- add Group to make EL5 happy

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-1
- new upstream release

* Tue Aug 23 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-1
- initial package
