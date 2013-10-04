%{?scl:%scl_package php-pecl-memcache}
%{!?scl:%global pkg_name %{name}}
%{!?__pecl:     %{expand: %%global __pecl     %{_bindir}/pecl}}

%global pecl_name memcache

Summary:      Extension to work with the Memcached caching daemon
Name:         %{?scl_prefix}php-pecl-memcache
Version:      3.0.8
Release:      2%{?dist}
License:      PHP
Group:        Development/Languages
URL:          http://pecl.php.net/package/%{pecl_name}

Source:       http://pecl.php.net/get/%{pecl_name}-%{version}.tgz
Source2:      xml2changelog

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: %{?scl_prefix}php-devel
BuildRequires: %{?scl_prefix}php-pear
BuildRequires: zlib-devel

Requires(post): %{__pecl}
Requires(postun): %{__pecl}
Requires:     %{?scl_prefix}php(zend-abi) = %{php_zend_api}
Requires:     %{?scl_prefix}php(api) = %{php_core_api}

Provides:     %{?scl_prefix}php-pecl(%{pecl_name}) = %{version}
Provides:     %{?scl_prefix}php-pecl(%{pecl_name})%{?_isa} = %{version}
Provides:     %{?scl_prefix}php-%{pecl_name} = %{version}
Provides:     %{?scl_prefix}php-%{pecl_name}%{?_isa} = %{version}

# Filter private shared
%{?filter_provides_in: %filter_provides_in %{_libdir}/.*\.so$}
%{?filter_setup}


%description
Memcached is a caching daemon designed especially for
dynamic web applications to decrease database load by
storing objects in memory.

This extension allows you to work with memcached through
handy OO and procedural interfaces.

Memcache can be used as a PHP session handler.


%prep 
%setup -c -q

pushd %{pecl_name}-%{version}

# Chech version as upstream often forget to update this
extver=$(sed -n '/#define PHP_MEMCACHE_VERSION/{s/.* "//;s/".*$//;p}' php_memcache.h)
if test "x${extver}" != "x%{version}"; then
   : Error: Upstream version is now ${extver}, expecting %{version}.
   : Update the pdover macro and rebuild.
   exit 1
fi
popd

%{_bindir}/php %{SOURCE2} package.xml | tee CHANGELOG | head -n 5

cat >%{pecl_name}.ini << 'EOF'
; ----- Enable %{pecl_name} extension module
extension=%{pecl_name}.so

; ----- Options for the %{pecl_name} module
; see http://www.php.net/manual/en/memcache.ini.php

;  Whether to transparently failover to other servers on errors
;memcache.allow_failover=1
;  Data will be transferred in chunks of this size
;memcache.chunk_size=32768
;  Autocompress large data
;memcache.compress_threshold=20000
;  The default TCP port number to use when connecting to the memcached server 
;memcache.default_port=11211
;  Hash function {crc32, fnv}
;memcache.hash_function=crc32
;  Hash strategy {standard, consistent}
;memcache.hash_strategy=consistent
;  Defines how many servers to try when setting and getting data.
;memcache.max_failover_attempts=20
;  The protocol {ascii, binary} : You need a memcached >= 1.3.0 to use the binary protocol
;  The binary protocol results in less traffic and is more efficient
;memcache.protocol=ascii
;  Redundancy : When enabled the client sends requests to N servers in parallel
;memcache.redundancy=1
;memcache.session_redundancy=2
;  Lock Timeout
;memcache.lock_timeout = 15

; ----- Options to use the memcache session handler

; RPM note : save_handler and save_path are defined
; for mod_php, in /etc/httpd/conf.d/php.conf
; for php-fpm, in /etc/php-fpm.d/*conf

;  Use memcache as a session handler
;session.save_handler=memcache
;  Defines a comma separated of server urls to use for session storage
;session.save_path="tcp://localhost:11211?persistent=1&weight=1&timeout=1&retry_interval=15"
EOF


%build
cd %{pecl_name}-%{version}
%{_bindir}/phpize
%configure --with-php-config=%{_bindir}/php-config
make %{?_smp_mflags}


%install
make -C %{pecl_name}-%{version} \
     install INSTALL_ROOT=%{buildroot}

# Drop in the bit of configuration
install -D -m 644 %{pecl_name}.ini %{buildroot}%{_sysconfdir}/php.d/%{pecl_name}.ini

# Install XML package description
install -Dpm 644 package.xml %{buildroot}%{pecl_xmldir}/%{pkg_name}.xml


%check
cd %{pecl_name}-%{version}
# simple module load test
%{_bindir}/php --no-php-ini \
    --define extension_dir=%{buildroot}%{php_extdir} \
    --define extension=%{pecl_name}.so \
    --modules | grep %{pecl_name}


%post
%{pecl_install} %{pecl_xmldir}/%{pkg_name}.xml >/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    %{pecl_uninstall} %{pecl_name} >/dev/null || :
fi


%files
%defattr(-,root,root,-)
%doc CHANGELOG %{pecl_name}-%{version}/{CREDITS,README,LICENSE}
%doc %{pecl_name}-%{version}/example.php %{pecl_name}-%{version}/memcache.php
%config(noreplace) %{_sysconfdir}/php.d/%{pecl_name}.ini
%{php_extdir}/%{pecl_name}.so
%{pecl_xmldir}/%{pkg_name}.xml


%changelog
* Thu Jul 18 2013 Remi Collet <rcollet@redhat.com> - 3.0.8-2
- rebuild for new value of php(zend-abi) and php(api) #985353

* Wed Apr 10 2013 Remi Collet <rcollet@redhat.com> - 3.0.8-1
- Update to 3.0.8

* Fri Dec 29 2012 Remi Collet <remi@fedoraproject.org> - 3.0.7-5
- add patch for https://bugs.php.net/59602
  segfault in getExtendedStats
- also provides php-memcache

* Thu Nov 15 2012 Remi Collet <remi@fedoraproject.org> - 3.0.7-4
- improve comment in configuration about session.

* Tue Oct 23 2012 Remi Collet <rcollet@redhat.com> 3.0.7-1.1
- fix RHEL-5 build (add buildroot + defattr)

* Wed Oct  3 2012 Remi Collet <rcollet@redhat.com> 3.0.7-1
- initial spec rewrite for scl build

* Tue Sep 25 2012 Remi Collet <remi@fedoraproject.org> - 3.0.7-3
- switch back to previous patch as possible memleak
  more acceptable than certain segfault

* Sun Sep 23 2012 Remi Collet <remi@fedoraproject.org> - 3.0.7-2
- use upstream patch instead of our (memleak)

* Sun Sep 23 2012 Remi Collet <remi@fedoraproject.org> - 3.0.7-1
- update to 3.0.7
- drop patches merged upstream
- cleanup spec

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul  5 2012 Joe Orton <jorton@redhat.com> - 3.0.6-4
- fix php_stream_cast() usage
- fix memory corruption after unserialization (Paul Clifford)
- package license

* Thu Jan 19 2012 Remi Collet <remi@fedoraproject.org> - 3.0.6-3
- rebuild against PHP 5.4, with patch
- fix filters

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Apr 11 2011 Remi Collet <Fedora@FamilleCollet.com> 3.0.6-1
- update to 3.0.6

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 23 2010  Remi Collet <Fedora@FamilleCollet.com> 3.0.5-2
- add filter_provides to avoid private-shared-object-provides memcache.so

* Tue Oct 05 2010 Remi Collet <Fedora@FamilleCollet.com> 3.0.5-1
- update to 3.0.5

* Thu Sep 30 2010 Remi Collet <Fedora@FamilleCollet.com> 3.0.4-4
- patch for bug #599305 (upstream #17566)
- add minimal load test in %%check

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 12 2009 Remi Collet <Fedora@FamilleCollet.com> 3.0.4-2
- rebuild for new PHP 5.3.0 ABI (20090626)

* Sat Feb 28 2009 Remi Collet <Fedora@FamilleCollet.com> 3.0.4-1
- new version 3.0.4

* Tue Jan 13 2009 Remi Collet <Fedora@FamilleCollet.com> 3.0.3-1
- new version 3.0.3

* Fri Sep 11 2008 Remi Collet <Fedora@FamilleCollet.com> 3.0.2-1
- new version 3.0.2

* Fri Sep 11 2008 Remi Collet <Fedora@FamilleCollet.com> 2.2.4-1
- new version 2.2.4 (bug fixes)

* Sat Feb  9 2008 Remi Collet <Fedora@FamilleCollet.com> 2.2.3-1
- new version

* Thu Jan 10 2008 Remi Collet <Fedora@FamilleCollet.com> 2.2.2-1
- new version

* Thu Nov 01 2007 Remi Collet <Fedora@FamilleCollet.com> 2.2.1-1
- new version

* Sat Sep 22 2007 Remi Collet <Fedora@FamilleCollet.com> 2.2.0-1
- new version
- add new INI directives (hash_strategy + hash_function) to config
- add BR on php-devel >= 4.3.11 

* Mon Aug 20 2007 Remi Collet <Fedora@FamilleCollet.com> 2.1.2-1
- initial RPM

