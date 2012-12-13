BuildRoot: %{_tmppath}/%{name}-root
Name: nodejs
Version: 0.8.15
Release: 1%{?dist}
Summary: JavaScript runtime
License: MIT
Group: Development/Languages
BuildRequires: python26
URL: http://nodejs.org/
Source0: http://nodejs.org/dist/v%{version}/node-v%{version}.tar.gz
Obsoletes: nodejs nodejs-devel nodejs-waf nodejs-compat-symlinks 
Obsoletes: nodejs-inherits nodejs-fstream nodejs-lru-cache nodejs-nopt nodejs-glob 
Obsoletes: nodejs-chownr nodejs-ansi nodejs-fast-list 
Obsoletes: nodejs-rimraf nodejs-mkdirp nodejs-block-stream nodejs-which nodejs-minimatch nodejs-abbrev 
Obsoletes: nodejs-semver nodejs-fstream-npm nodejs-graceful-fs nodejs-tar nodejs-request nodejs-fstream-ignore 
Obsoletes: nodejs-uid-number nodejs-ini nodejs-archy nodejs-proto-list nodejs-read nodejs-node-uuid 
Obsoletes: nodejs-slide-flow-control

%description
Node.js is a platform built on Chrome's JavaScript runtime
for easily building fast, scalable network applications.
Node.js uses an event-driven, non-blocking I/O model that
makes it lightweight and efficient, perfect for data-intensive
real-time applications that run across distributed devices.


%prep
%setup -q -n node-v%{version}
sed -i -e "s/\/usr\/bin\/env python/\/usr\/bin\/env python2.6/" configure

%build
export PYTHON=python2.6 
./configure --prefix=%{_prefix} --without-waf --without-dtrace
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
export PYTHON=python2.6 
export DESTDIR=$RPM_BUILD_ROOT
make INSTALL='install -p' install

# and remove dtrace file again
rm -rf $RPM_BUILD_ROOT/%{_prefix}/lib/dtrace

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog LICENSE README.md AUTHORS
%{_bindir}/node
%{_bindir}/npm
%{_mandir}/man1/node.*
%dir %{_includedir}/node/
%{_includedir}/node/*.h
%dir %{_includedir}/node/uv-private/
%{_includedir}/node/uv-private/*.h
%{_mandir}/man1/node.1.gz
%dir /usr/lib/node_modules
/usr/lib/node_modules/*

%changelog
* Wed Dec 12 2012 Erik LaBianca <erik.labianca@gmail.com> - 0.8.15-1
- RHEL5 compatiblity:
-   go back to bundled dependencies to allow for building on old systems
-   force build using python2.6 to keep new-style references happy
-   revert back to 0.8.15 in order to resolve gcc incompatiblity problems with 0.9
-   include npm in the package

* Wed Nov 28 2012 Stephen Gallagher <sgallagh@redhat.com> - 0.9.3-4
- Rename binary and manpage to nodejs

* Mon Nov 19 2012 Stephen Gallagher <sgallagh@redhat.com> - 0.9.3-3
- Update to latest upstream development release 0.9.3
- Include upstreamed patches to unbundle dependent libraries

* Tue Oct 23 2012 Adrian Alves <alvesadrian@fedoraproject.org>  0.8.12-1
- Fixes and Patches suggested by Matthias Runge

* Mon Apr 09 2012 Adrian Alves <alvesadrian@fedoraproject.org> 0.6.5
- First build.

