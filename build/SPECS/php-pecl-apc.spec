%if 0%{?scl:1}
%scl_package php-pecl-apc
%else
%global pkg_name          %{name}
%global _root_sysconfdir  %{_sysconfdir}
%endif
%{!?__pecl: %{expand: %%global __pecl %{_bindir}/pecl}}

%global pecl_name APC
%global svnrev 329724
# TODO rev >= 329725 have opcache default on (so need to be fixed)

Summary:       APC caches and optimizes PHP intermediate code
Name:          %{?scl_prefix}php-pecl-apc
Version:       3.1.15
Release:       0.2.svn%{svnrev}%{?dist}
License:       PHP
Group:         Development/Languages
URL:           http://pecl.php.net/package/APC
# svn export -r 329724 http://svn.php.net/repository/pecl/apc/trunk APC-3.1.15
# tar czf APC-3.1.15-dev.tgz APC-3.1.15
Source0: http://pecl.php.net/get/APC-%{version}%{?svnrev:-dev}.tgz
Source1:       apc.ini
Source2:       apc-panel.conf
Source3:       apc.conf.php

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: httpd-devel
BuildRequires: %{?scl_prefix}php-devel
BuildRequires: %{?scl_prefix}php-pear
# Only for tests (used by some unit tests)
BuildRequires: %{?scl_prefix}php-dom

Requires(post): %{__pecl}
Requires(postun): %{__pecl}
Requires:      %{?scl_prefix}php(zend-abi) = %{php_zend_api}
Requires:      %{?scl_prefix}php(api) = %{php_core_api}

Provides:      %{?scl_prefix}php-apc = %{version}
Provides:      %{?scl_prefix}php-apc%{?_isa} = %{version}
Provides:      %{?scl_prefix}php-pecl(%{pecl_name}) = %{version}
Provides:      %{?scl_prefix}php-pecl(%{pecl_name})%{?_isa} = %{version}

# Filter private shared
%{?filter_provides_in: %filter_provides_in %{_libdir}/.*\.so$}
%{?filter_setup}


%description
APC is a free, open, and robust framework for caching and optimizing PHP
intermediate code.


%package devel
Summary:       APC developer files (header)
Group:         Development/Libraries
Requires:      %{?scl_prefix}php-pecl-apc%{?_isa} = %{version}-%{release}
Requires:      %{?scl_prefix}php-devel%{?_isa}

%description devel
These are the files needed to compile programs using APC serializer.


%package -n %{?scl_prefix}apc-panel
Summary:       APC control panel
Group:         Applications/Internet
%if 0%{?fedora} >= 12 || 0%{?rhel} >= 6
BuildArch:     noarch
%endif
Requires:      %{name} = %{version}-%{release}
Requires:      %{?scl_prefix}mod_php
Requires:      %{?scl_prefix}php-gd
Requires:      httpd

%description  -n %{?scl_prefix}apc-panel
This package provides the APC control panel, with Apache
configuration, available on http://localhost/apc-panel/


%prep
%setup -q -c
%if 0%{?svnrev}
sed -e "/release/s/%{version}/%{version}dev/" \
    -e "/date/s/2013-??-??/2013-03-10/" \
    APC-%{version}/package.xml >package.xml
grep date package.xml
%endif

cd APC-%{version}

%if 0%{?__isa_bits}
# port number to allow 32/64 build at same time
port=$(expr %{__isa_bits} + 8900)
sed -e "/PHP_CLI_SERVER_PORT/s/8964/$port/" \
    -i tests/server_test.inc
%endif

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_APC_VERSION/{s/.* "//;s/".*$//;p}' php_apc.h)
if test "x${extver}" != "x%{version}%{?svnrev:-dev}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?svnrev:-dev}..
   exit 1
fi
cd ..

%if 0%{?__ztsphp:1}
# duplicate for ZTS build
cp -pr APC-%{version} APC-%{version}-zts
%endif


%build
cd APC-%{version}
%{_bindir}/phpize
%configure --enable-apc-mmap --with-php-config=%{_bindir}/php-config
make %{?_smp_mflags}

%if 0%{?__ztsphp:1}
cd ../APC-%{version}-zts
%{_bindir}/zts-phpize
%configure --enable-apc-mmap --with-php-config=%{_bindir}/zts-php-config
make %{?_smp_mflags}
%endif


%install
# Install the NTS stuff
pushd APC-%{version}
make install INSTALL_ROOT=%{buildroot}

# Fix the charset of NOTICE
iconv -f iso-8859-1 -t utf8 NOTICE >NOTICE.utf8
mv NOTICE.utf8 NOTICE
popd
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/php.d/apc.ini

# Install the ZTS stuff
%if 0%{?__ztsphp:1}
pushd APC-%{version}-zts
make install INSTALL_ROOT=%{buildroot}
popd
install -D -m 644 %{SOURCE1} %{buildroot}%{php_ztsinidir}/apc.ini
%endif

# Install the package XML file
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# Install the Control Panel
# Pages
install -d -m 755 %{buildroot}%{_datadir}/apc-panel
sed -e s:apc.conf.php:%{_sysconfdir}/apc-panel/conf.php:g \
    APC-%{version}/apc.php >%{buildroot}%{_datadir}/apc-panel/index.php
# Apache config
install -D -m 644 -p %{SOURCE2} \
        %{buildroot}%{_root_sysconfdir}/httpd/conf.d/%{?scl_prefix}apc-panel.conf
sed -e 's:/usr/share:%{_datadir}:' \
    -i %{buildroot}%{_root_sysconfdir}/httpd/conf.d/%{?scl_prefix}apc-panel.conf

# Panel config
install -D -m 644 -p %{SOURCE3} \
        %{buildroot}%{_sysconfdir}/apc-panel/conf.php


%check
%ifarch x86_64
cd %{pecl_name}-%{version}
ln -sf %{php_extdir}/dom.so modules/

TEST_PHP_EXECUTABLE=%{_bindir}/php \
TEST_PHP_ARGS="-n -d extension_dir=$PWD/modules -d extension=dom.so -d extension=apc.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=0 \
%{_bindir}/php -n run-tests.php

%if 0%{?__ztsphp:1}
cd ../%{pecl_name}-%{version}-zts
ln -sf %{php_ztsextdir}/dom.so modules/

TEST_PHP_EXECUTABLE=%{__ztsphp} \
TEST_PHP_ARGS="-n -d extension_dir=$PWD/modules -d extension=dom.so -d extension=apc.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=0 \
%{__ztsphp} -n run-tests.php
%endif
%else
: minimal load test
%{_bindir}/php -n \
   -d extension_dir=%{pecl_name}-%{version}/modules \
   -d extension=apc.so -m | grep apc
%if 0%{?__ztsphp:1}
%{__ztsphp}    -n \
   -d extension_dir=%{pecl_name}-%{version}-zts/modules \
   -d extension=apc.so -m | grep apc
%endif
%endif


%post
%{pecl_install} %{pecl_xmldir}/%{name}.xml >/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    %{pecl_uninstall} %{pecl_name} >/dev/null || :
fi


%files
%defattr(-,root,root,-)
%doc APC-%{version}/TECHNOTES.txt APC-%{version}/CHANGELOG APC-%{version}/LICENSE
%doc APC-%{version}/NOTICE        APC-%{version}/TODO      APC-%{version}/apc.php
%doc APC-%{version}/INSTALL
%config(noreplace) %{_sysconfdir}/php.d/apc.ini
%{php_extdir}/apc.so
%{pecl_xmldir}/%{name}.xml

%if 0%{?__ztsphp:1}
%{php_ztsextdir}/apc.so
%config(noreplace) %{php_ztsinidir}/apc.ini
%endif

%files devel
%defattr(-,root,root,-)
%{_includedir}/php/ext/apc

%if 0%{?__ztsphp:1}
%defattr(-,root,root,-)
%{php_ztsincldir}/ext/apc
%endif

%files -n %{?scl_prefix}apc-panel
%defattr(-,root,root,-)
# Need to restrict access, as it contains a clear password
%attr(750,apache,root) %dir %{_sysconfdir}/apc-panel
%config(noreplace) %{_sysconfdir}/apc-panel/conf.php
%config(noreplace) %{_root_sysconfdir}/httpd/conf.d/%{?scl_prefix}apc-panel.conf
%{_datadir}/apc-panel


%changelog
* Thu Jul 18 2013 Remi Collet <rcollet@redhat.com> - 3.1.15-0.2.svn329724
- rebuild for new value of php(zend-abi) and php(api) #985352

* Fri Mar 15 2013 Remi Collet <remi@fedoraproject.org> - 3.1.15-0.1.svn329724
- update to 3.1.15dev with new directive 'enable_opcode_cache' (disabled)
  which allow to cache only user data and use another opcode cache
- switch most configuration to upstream default

* Thu Jan  3 2013 Remi Collet <remi@fedoraproject.org> - 3.1.14-1
- Version 3.1.14 (beta) - API 3.1.0 (stable)
- apc-panel requires php-gd
- also provides php-apc

* Mon Nov 19 2012 Remi Collet <rcollet@redhat.com> 3.1.13-3
- rebuild for php and system pcre
- only run test on x86_64

* Thu Nov 15 2012 Remi Collet <rcollet@redhat.com> 3.1.13-2
- initial spec rewrite for scl build
- fix RHEL-5 build (add buildroot + defattr)

* Fri Oct 26 2012 Remi Collet <remi@fedoraproject.org> - 3.1.13-2
- move apc.ini to Source3
- new apc-panel package

* Mon Sep  3 2012 Remi Collet <remi@fedoraproject.org> - 3.1.13-1
- Version 3.1.13 (beta) - API 3.1.0 (stable)
- add patches from upstream (fixes some tests)
- change serveur port for tests (allow 32/64 bits build)

* Mon Aug 27 2012 Remi Collet <remi@fedoraproject.org> - 3.1.12-2
- add patches from upstream
- delete tests which fail because of missing dom extension

* Thu Aug 16 2012 Remi Collet <remi@fedoraproject.org> - 3.1.12-1
- Version 3.1.12 (beta) - API 3.1.0 (stable)
- spec cleanups

* Fri Jul 20 2012 Remi Collet <remi@fedoraproject.org> - 3.1.11-1
- update to 3.1.11 (beta)

* Fri Jun 22 2012 Remi Collet <remi@fedoraproject.org> - 3.1.10-2
- add patches from upstream

* Wed Apr 11 2012 Remi Collet <remi@fedoraproject.org> - 3.1.10-1
- Update to 3.1.10 (beta)
- fix reported version, https://bugs.php.net/61696

* Thu Mar 15 2012 Remi Collet <remi@fedoraproject.org> - 3.1.9-6.svn324146
- new SVN snapshot
- enable ZTS build

* Sat Feb 18 2012 Remi Collet <remi@fedoraproject.org> - 3.1.9-5.svn322617
- rebuild against php 5.4.0RC8 (without zend-signals)
- pull latest SVN changes

* Thu Jan 19 2012 Remi Collet <remi@fedoraproject.org> - 3.1.9-4.svn316786
- rebuild against php 5.4
- keep apc.php as doc
- fix filters

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Jeroen van Meeuwen <kanarip@kanarip.com> - 3.1.9-2
- Ship apc.php in a static location as well, so that it is easier to
  refer to in webserver configuration files (monitoring...)
- Fix the apostrophes messing with the syntax highlighting of your
  favorite editor

* Sun May 15 2011 Remi Collet <Fedora@FamilleCollet.com> - 3.1.9-1
- update to 3.1.9 (bugfix, stable)

* Sat May 14 2011 Remi Collet <Fedora@FamilleCollet.com> - 3.1.8-2
- fix for http://pecl.php.net/bugs/22687

* Tue May  3 2011 Remi Collet <Fedora@FamilleCollet.com> - 3.1.8-1
- update to 3.1.8 (bugfix, stable)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Remi Collet <Fedora@FamilleCollet.com> - 3.1.7-1
- update to 3.1.7 (bugfix)
- add devel subpackage (for serializer)

* Tue Nov 30 2010 Remi Collet <Fedora@FamilleCollet.com> - 3.1.6-1
- update to 3.1.6 (bugfix)

* Wed Nov 03 2010 Remi Collet <Fedora@FamilleCollet.com> - 3.1.5-2
- fix reported version, see http://pecl.php.net/bugs/19590

* Wed Nov 03 2010 Remi Collet <Fedora@FamilleCollet.com> - 3.1.5-1
- update to 3.1.5 (bugfix)

* Sat Oct 23 2010 Remi Collet <Fedora@FamilleCollet.com> - 3.1.4-3
- add filter_provides to avoid private-shared-object-provides apc.so

* Sun Aug 08 2010 Remi Collet <Fedora@FamilleCollet.com> - 3.1.4-2
- fix default value for apc.shm_size (need M suffixes)

* Thu Aug 05 2010 Remi Collet <Fedora@FamilleCollet.com> - 3.1.4-1
- update to Version 3.1.4 (beta) - API 3.1.0 (beta)

* Fri Aug 14 2009 Remi Collet <Fedora@FamilleCollet.com> - 3.1.3p1-1
- update to 3.1.3 patch1 (beta, for PHP 5.3 support)
- add test suite (disabled for http://pecl.php.net/bugs/bug.php?id=16793)
- add use_request_time, lazy_classes, lazy_functions options (apc.ini)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 12 2009 Remi Collet <Fedora@FamilleCollet.com> - 3.1.2-1
- update to 3.1.2 (beta) - PHP 5.3 support
- use setup -q -c

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jun 25 2008 Tim Jackson <rpm@timj.co.uk> - 3.0.19-1
- Update to 3.0.19
- Fix PHP Zend API/ABI dependencies to work on EL-4/5
- Fix "License" tag
- Fix encoding of "NOTICE" file
- Add registration via PECL

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.0.14-3
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 3.0.14-2
- Rebuild for selinux ppc32 issue.

* Thu Jun 28 2007 Chris Chabot <chabotc@xs4all.nl> - 3.0.14-1
- Updated to 3.0.14
- Included new php api snipplets

* Fri Sep 15 2006 Chris Chabot <chabotc@xs4all.nl> - 3.0.12-5
- Updated to new upstream version

* Mon Sep 11 2006 Chris Chabot <chabotc@xs4all.nl> - 3.0.10-5
- FC6 rebuild 

* Sun Aug 13 2006 Chris Chabot <chabotc@xs4all.nl> - 3.0.10-4
- FC6T2 rebuild

* Mon Jun 19 2006 - Chris Chabot <chabotc@xs4all.nl> - 3.0.10-3
- Renamed to php-pecl-apc and added provides php-apc
- Removed php version string from the package version

* Mon Jun 19 2006 - Chris Chabot <chabotc@xs4all.nl> - 3.0.10-2
- Trimmed down BuildRequires
- Added Provices php-pecl(apc)

* Sun Jun 18 2006 - Chris Chabot <chabotc@xs4all.nl> - 3.0.10-1
- Initial package, templated on already existing php-json 
  and php-eaccelerator packages
