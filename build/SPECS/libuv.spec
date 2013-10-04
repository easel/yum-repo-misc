%{?scl:%scl_package libuv}
%{!?scl:%global pkg_name %{name}}

%global git_snapshot 5462dab

#we only need major.minor in the SONAME in the stable (even numbered) series
#this should be changed to %%{version} in unstable (odd numbered) releases
%global sover 0.10

Name: %{?scl_prefix}libuv
Epoch:   1
Version: 0.10.5
Release: 1.1%{?dist}
Summary: Platform layer for node.js

Group: Development/Tools
License: MIT
URL: http://nodejs.org/
Source0: http://libuv.org/dist/v%{version}/%{pkg_name}-v%{version}.tar.gz
Source2: libuv.pc.in

%{?scl:Requires: %{scl}-runtime}
BuildRequires: %{?scl_prefix}gyp
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

# Bundling exception request:
# https://fedorahosted.org/fpc/ticket/231
Provides: %{?scl_prefix}bundled(libev) = 4.04

%description
libuv is a new platform layer for Node. Its purpose is to abstract IOCP on
Windows and libev on Unix systems. We intend to eventually contain all platform
differences in this library.

%package devel
Summary: Development libraries for libuv
Group: Development/Tools
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: pkgconfig
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description devel
Development libraries for libuv

%prep
%setup -q -n %{pkg_name}-v%{version}

%build
%{?scl:scl enable %{scl} "}
export CFLAGS='%{optflags}'
export CXXFLAGS='%{optflags}'
./gyp_uv -Dcomponent=shared_library -Dlibrary=shared_library

# Modify the build so it produces a versioned shared library
pushd out
mv libuv.target.mk libuv.target.mk.orig
sed "s/libuv.so/libuv.so.%{sover}/g" libuv.target.mk.orig > libuv.target.mk
mv run-benchmarks.target.mk run-benchmarks.target.mk.orig
sed "s/libuv.so/libuv.so.%{sover}/g" run-benchmarks.target.mk.orig > run-benchmarks.target.mk
mv run-tests.target.mk run-tests.target.mk.orig
sed "s/libuv.so/libuv.so.%{sover}/g" run-tests.target.mk.orig > run-tests.target.mk
popd

make %{?_smp_mflags} V=1 -C out BUILDTYPE=Release
%{?scl: "}

%install
# Copy the shared lib into the libdir
mkdir -p %{buildroot}/%{_libdir}/
cp out/Release/obj.target/libuv.so.%{sover} %{buildroot}/%{_libdir}/libuv.so.%{sover}
pushd %{buildroot}/%{_libdir}/
ln -s libuv.so.%{sover} libuv.so.0
ln -s libuv.so.%{sover} libuv.so
popd

# Copy the headers into the include path
mkdir -p %{buildroot}/%{_includedir}/uv-private

cp include/uv.h \
   %{buildroot}/%{_includedir}

cp \
   include/uv-private/ngx-queue.h \
   include/uv-private/tree.h \
   include/uv-private/uv-linux.h \
   include/uv-private/uv-unix.h \
   %{buildroot}/%{_includedir}/uv-private

# Create the pkgconfig file
mkdir -p %{buildroot}/%{_libdir}/pkgconfig

sed -e "s#@prefix@#%{_prefix}#g" \
    -e "s#@exec_prefix@#%{_exec_prefix}#g" \
    -e "s#@libdir@#%{_libdir}#g" \
    -e "s#@includedir@#%{_includedir}#g" \
    -e "s#@version@#%{version}.git%{git_snapshot}#g" \
    %SOURCE2 > %{buildroot}/%{_libdir}/pkgconfig/libuv.pc

%check
# Tests are currently disabled because some require network access
# Working with upstream to split these out
#./run-tests
#./run-benchmarks

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md AUTHORS LICENSE
%{_libdir}/libuv.so.*

%files devel
%doc README.md AUTHORS LICENSE
%{_libdir}/libuv.so
%{_libdir}/pkgconfig/libuv.pc
%{_includedir}/uv.h
%{_includedir}/uv-private

%changelog
* Wed May 15 2013 Tomas Hrcka <thrcka@redhat.com> - 1:0.10.5-1.1
- updated to upstream stable vedsion

* Wed Apr 24 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.5-1
- new upstream release 0.10.5

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.4-1
- new upstream release 0.10.4
- drop upstreamed patch

* Fri Apr 05 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:0.10.3-3
- Add support for software collections

* Thu Apr 04 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.3-2
- backport patch that fixes FTBFS in nodejs-0.10.3

* Sun Mar 31 2013 tchollingsworth@gmail.com - 1:0.10.3-1
- rebase to 0.10.3
- upstream now does proper releases

* Tue Mar 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.0-2.git5462dab
- drop the patchlevel from the SONAME since libuv will retain binary
  compatibility for the life of the 0.10.x series

* Mon Mar 11 2013 Stephen Gallagher <sgallagh@redhat.com> - 1:0.10.0-1.git5462dab
- Upgrade to 0.10.0 release to match stable Node.js release

* Thu Feb 28 2013 Stephen Gallagher <sgallagh@redhat.com> - 1:0.9.4-4.gitdc559a5
- Bump epoch for the version downgrade
- The 0.9.7 version hit the Rawhide repo due to the mass rebuild, we need a
  clean upgrade path.

* Thu Feb 21 2013 Stephen Gallagher <sgallagh@redhat.com> - 0.9.4-3.gitdc559a5
- Revert to version 0.9.4 (since 0.9.7 is breaking builds)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2.git4ba03dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Stephen Gallagher <sgallagh@redhat.com> - 0.9.7-1.git4ba03dd
- Bump to version included with Node.js 0.9.7

* Wed Dec 26 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.4-0.1.gitdc559a5
- bump to version included with node 0.9.4
- drop upstreamed patch
- respect optflags

* Thu Nov 15 2012 Stephen Gallagher <sgallagh@redhat.com> - 0.9.3-0.3.git09b0222
- Add patch to export uv_inet_*

* Wed Nov 14 2012 Stephen Gallagher <sgallagh@redhat.com> - 0.9.3-0.2.git09b0222
- Fixes from package review
- Removed doubly-listed include directory
- Update git tarball to the latest upstream code

* Thu Nov 08 2012 Stephen Gallagher <sgallagh@redhat.com> - 0.9.3-0.1.gitd56434a
- Initial package
