%{?scl:%scl_package node-gyp}
%{!?scl:%global pkg_name %{name}}

%nodejs_find_provides_and_requires

Name:       %{?scl_prefix}node-gyp
Version:    0.9.5
Release:    3%{?dist}
Summary:    Node.js native addon build tool
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/TooTallNate/node-gyp
Source0:    http://registry.npmjs.org/node-gyp/-/node-gyp-%{version}.tgz
Source1:    addon-rpm.gypi
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

# These patches are Fedora-specific for the moment, although I'd like to find
# a way to support this kind of stuff upstream.

# use RPM installed headers by default instead of downloading a source tree
# for the currently running node version
Patch1:     node-gyp-addon-gypi.patch

# use the system gyp
Patch2:     node-gyp-system-gyp.patch

BuildRequires:  %{?scl_prefix}nodejs-devel

#gyp is the actual build framework node-gyp uses
Requires: %{?scl_prefix}gyp
#this is the standard set of headers expected to build any node native module
Requires: %{?scl_prefix}nodejs-devel %{?scl_prefix}v8-devel %{?scl_prefix}libuv-devel %{?scl_prefix}http-parser-devel
#we also need a C++ compiler to actually build stuff ;-)
Requires: gcc-c++

%description
node-gyp is a cross-platform command-line tool written in Node.js for compiling
native addon modules for Node.js, which takes away the pain of dealing with the
various differences in build platforms. It is the replacement to the node-waf
program which is removed for node v0.8.

%prep
%setup -q -n package

sed -i 's:/usr:%{_prefix}:g' %PATCH1 %PATCH2 %{SOURCE1}
%patch1 -p1
%patch2 -p1

%nodejs_fixdep request

#remove the bundled gyp
rm -rf gyp

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/node-gyp
cp -pr addon*.gypi bin lib legacy package.json %{buildroot}%{nodejs_sitelib}/node-gyp
cp -p %{SOURCE1} %{buildroot}%{nodejs_sitelib}/node-gyp/addon-rpm.gypi

mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/node-gyp/bin/node-gyp.js %{buildroot}%{_bindir}/node-gyp

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/node-gyp
%{_bindir}/node-gyp
%doc README.md LICENSE

%changelog
* Fri Apr 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.9.5-3
- Use proper prefixed paths for gyp

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.9.5-2
- Add support for software collections

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-1
- new upstream release 0.9.5

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.1-2
- update addon-rpm.gypi
- split out addon-rpm.gypi so it's easier to maintain

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.1-1
- new upstream release 0.9.1

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.4-1
- new upstream release 0.8.4

* Mon Jan 21 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.3-1
- new upstream release 0.8.3
- add missing Requires on http-parser-devel

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.2-3
- add missing build section

* Sat Jan 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.2-2
- use RPM-installed headers by default
- now patched to use the system gyp instead of relying on a symlink

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.2-1
- new upstream release 0.8.2
- clean up for submission

* Thu Apr 26 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.1-2
- fix dependencies

* Wed Apr 18 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.1-1
- New upstream release 0.4.1

* Fri Apr 06 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.11-1
- New upstream release 0.3.11

* Mon Apr 02 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.10-1
- New upstream release 0.3.10

* Thu Mar 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.9-1
- New upstream release 0.3.9

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.8-1
- new upstream release 0.3.8

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.7-1
- new upstream release 0.3.7

* Thu Mar 15 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.5-1
- initial package
