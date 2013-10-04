%{?scl:%scl_package nodejs-graceful-fs}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}
Name:       %{?scl_prefix}nodejs-graceful-fs
Version:    1.2.1
Release:    2.1%{?dist}
Summary:    'fs' module with incremental back-off on EMFILE
# The license was previously ambiguous, but the author has now clarified that
# it is BSD (not MIT).
License:    BSD
Group:      Development/Libraries
URL:        https://github.com/isaacs/node-graceful-fs
Source0:    http://registry.npmjs.org/graceful-fs/-/graceful-fs-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
# The LICENSE file has been updated upstream to reflect the actual license.
Source1:    LICENSE
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Just like node.js' fs module, but it does an incremental back-off when EMFILE is
encountered.  Useful in asynchronous situations where one needs to try to open
lots and lots of files.

%prep
%setup -q -n package
rm -f LICENSE
cp -a %{SOURCE1} .

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/graceful-fs
cp -p graceful-fs.js package.json %{buildroot}%{nodejs_sitelib}/graceful-fs

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/graceful-fs
%doc README.md LICENSE

%changelog
* Tue May 28 2013 Tomas Hrcka <thrcka@redhat.com> - 1.2.1-2.1
- merged latest upstream release and fix BZ#967550

* Mon May 27 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.1-2
- the LICENSE file previously contained the wrong license (MIT), but now
  upstream have fixed it to contain the correct license (BSD) (#967442)

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.1-1
- update to upstream release 1.2.1

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.0-2
- add macro for EPEL6 dependency generation

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.0-2
- Add support for software collections

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.0-1
- new upstream release 1.2.0

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.14-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.14-1
- new upstream release 1.1.14
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.8-2
- guard Requires for F17 automatic depedency generation

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.8-1
- new upstream release 1.1.8

* Sun Jan 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.5-1
- new upstream release 1.1.5

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-2
- missing Group field for EL5

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-1
- new upstream release 1.1.4

* Thu Nov 10 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-0.1.20111109git33dee97
- new upstream release
- Node v0.6.0 compatibility fixes

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.1-1
- new upstream release

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-1
- initial package
