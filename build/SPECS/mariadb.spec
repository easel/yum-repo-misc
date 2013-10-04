%{?scl:%scl_package mariadb}

Name: %{?scl_prefix}mariadb
Version: 5.5.32
Release: 1%{?dist}

Summary: A community developed branch of MySQL
Group: Applications/Databases
URL: http://mariadb.org
# Exceptions allow client libraries to be linked with most open source SW,
# not only GPL code.  See README.mysql-license
# Some innobase code from Percona and Google is under BSD license
# Some code related to test-suite is under LGPLv2
License: GPLv2 with exceptions and LGPLv2 and BSD

# Regression tests take a long time, you can skip 'em with this
%{!?runselftest:%global runselftest 1}

Source0: http://ftp.osuosl.org/pub/mariadb/mariadb-%{version}/kvm-tarbake-jaunty-x86/mariadb-%{version}.tar.gz
Source3: my.cnf
Source5: my_config.h
Source6: README.mysql-docs
Source7: README.mysql-license
Source8: libmysql.version
Source14: rh-skipped-tests-base.list
Source15: rh-skipped-tests-arm.list
# Working around perl dependency checking bug in rpm FTTB. Remove later.
Source17: mysql.init
# We need to document how depended packages should be biult
Source18: README.mariadb-devel
Source999: filter-requires-mysql.sh

# Comments for these patches are in the patch files.
Patch1: mariadb-errno.patch
Patch2: mariadb-strmov.patch
Patch3: mariadb-install-test.patch
Patch4: mariadb-expired-certs.patch
Patch5: mariadb-versioning.patch
Patch6: mariadb-dubious-exports.patch
Patch7: mariadb-s390-tsc.patch
Patch8: mariadb-logrotate.patch
Patch9: mariadb-cipherspec.patch
Patch10: mariadb-file-contents.patch
Patch11: mariadb-string-overflow.patch
Patch12: mariadb-dh1024.patch
Patch14: mariadb-basedir.patch
Patch15: mariadb-covscan-signexpr.patch
Patch16: mariadb-covscan-stroverflow.patch
Patch101: mariadb-scl-env-check.patch
Patch102: mariadb-daemonstatus.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl, readline-devel, openssl-devel
BuildRequires: cmake, ncurses-devel, zlib-devel, libaio-devel
BuildRequires: systemtap-sdt-devel
# make test requires time and ps
BuildRequires: time procps
# perl modules needed to run regression tests
BuildRequires: perl(Socket), perl(Time::HiRes)
BuildRequires: perl(Data::Dumper), perl(Test::More), perl(Env)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: grep, fileutils, bash
%{?scl:Requires:%scl_runtime}

# When rpm 4.9 is universal, this could be cleaned up:
%global __perl_requires %{SOURCE999}
%global __perllib_requires %{SOURCE999}

# By default, patch(1) creates backup files when chunks apply with offsets.
# Turn that off to ensure such files don't get included in RPMs (cf bz#884755).
%global _default_patch_flags --no-backup-if-mismatch

%description
MariaDB is a community developed branch of MySQL.
MariaDB is a multi-user, multi-threaded SQL database server.
It is a client/server implementation consisting of a server daemon (mysqld)
and many different client programs and libraries. The base package
contains the standard MariaDB/MySQL client programs and generic MySQL files.

%package libs

Summary: The shared libraries required for MariaDB/MySQL clients
Group: Applications/Databases
%{?scl:Requires:%scl_runtime}

%description libs
The mariadb-libs package provides the essential shared libraries for any 
MariaDB/MySQL client program or interface. You will need to install this
package to use any other MariaDB package or any clients that need to connect
to a MariaDB/MySQL server. MariaDB is a community developed branch of MySQL.

%package server

Summary: The MariaDB server and related files
Group: Applications/Databases
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: sh-utils
Requires(pre): /usr/sbin/useradd
Requires(post): policycoreutils
# mysqlhotcopy needs DBI/DBD support
Requires: perl-DBI, perl-DBD-MySQL
%{?scl:Requires:%scl_runtime}

%description server
MariaDB is a multi-user, multi-threaded SQL database server. It is a
client/server implementation consisting of a server daemon (mysqld)
and many different client programs and libraries. This package contains
the MariaDB server and some accompanying files and directories.
MariaDB is a community developed branch of MySQL.

%package devel

Summary: Files for development of MariaDB plugins
Group: Applications/Databases
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: openssl-devel%{?_isa}

%description devel
MariaDB is a multi-user, multi-threaded SQL database server. This
package contains the libraries and header files that are needed for
developing MariaDB plugins.

%package bench

Summary: MariaDB benchmark scripts and data
Group: Applications/Databases
Requires: %{name}%{?_isa} = %{version}-%{release}
%{?scl:Requires:%scl_runtime}

%description bench
MariaDB is a multi-user, multi-threaded SQL database server. This
package contains benchmark scripts and data for use when benchmarking
MariaDB.
MariaDB is a community developed branch of MySQL.

%package test

Summary: The test suite distributed with MariaD
Group: Applications/Databases
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-server%{?_isa} = %{version}-%{release}
BuildRequires: perl(Socket), perl(Time::HiRes)
BuildRequires: perl(Data::Dumper), perl(Test::More), perl(Env)
%{?scl:Requires:%scl_runtime}

%description test
MariaDB is a multi-user, multi-threaded SQL database server. This
package contains the regression test suite distributed with
the MariaDB sources.
MariaDB is a community developed branch of MySQL.

%prep
%setup -q -n mariadb-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

# path fixes in source for dsc - using sed instead of patching, 
# because we would need various patches for various collections
sed -i -e 's|/etc/|%{_sysconfdir}/|g' mysys/default.c
sed -i -e 's|/etc/my|%{_sysconfdir}/my|g' scripts/mysqld_multi.sh
sed -i -e 's|/etc/|%{_sysconfdir}/|g' scripts/mysqlaccess.sh
sed -i -e 's|/usr/|%{_prefix}/|g' ./client/mysql_plugin.c
sed -i -e 's|/usr|%{_prefix}|g' ./mysql-test/t/file_contents.test
sed -i -e 's|/var/log/mysql|/var/log/%{?scl_prefix}mysql|g' support-files/mysql-log-rotate.sh

# path adding collection name into some scripts
# patch is applied only if building into SCL
# some values in patch are replaced by real value depending on collection name
cp -p %{SOURCE17} mysql.init
%if 0%{?scl:1}
%global scl_sed_patches 1
%if %scl_sed_patches
cat %{PATCH101} | sed -e "s/__SCL_NAME__/%{?scl}/g" \
       -e "s|__SCL_SCRIPTS__|%{?_scl_scripts}|g" \
       | patch -p1 -b --suffix .scl-env-check
cat %{PATCH102} | sed -e "s/__SCL_NAME__/%{?scl}/g" \
                | patch -p1 -b --suffix .daemonstatus
%else
patch -p1 -b --suffix .scl-env-check<%{PATCH101}
patch -p1 -b --suffix .daemonstatus<%{PATCH102}
%endif
%endif

# workaround for upstream bug #56342
rm -f mysql-test/t/ssl_8k_key-master.opt

# upstream has fallen down badly on symbol versioning, do it ourselves
cp -p %{SOURCE8} libmysql/libmysql.version

# generate a list of tests that fail, but are not disabled by upstream
cat %{SOURCE14} > mysql-test/rh-skipped-tests.list
# disable some tests failing on ARM architectures
%ifarch %{arm}
cat %{SOURCE15} >> mysql-test/rh-skipped-tests.list
%endif
# disable some tests failing on ppc and s390
%ifarch ppc ppc64 ppc64p7 s390 s390x
echo "main.gis-precise : rhbz#906367" >> mysql-test/rh-skipped-tests.list
%endif

%build

# fail quickly and obviously if user tries to build as root
%if %runselftest
	if [ x"`id -u`" = x0 ]; then
		echo "mariadb's regression tests fail if run as root."
		echo "If you really need to build the RPM as root, use"
		echo "--define='runselftest 0' to skip the regression tests."
		exit 1
	fi
%endif

CFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE"
# force PIC mode so that we can build libmysqld.so
CFLAGS="$CFLAGS -fPIC"
# gcc seems to have some bugs on sparc as of 4.4.1, back off optimization
# submitted as bz #529298
%ifarch sparc sparcv9 sparc64
CFLAGS=`echo $CFLAGS| sed -e "s|-O2|-O1|g" `
%endif
CXXFLAGS="$CFLAGS"
export CFLAGS CXXFLAGS
# building with PIE
LDFLAGS="$LDFLAGS -pie"
export LDFLAGS

# The INSTALL_xxx macros have to be specified relative to CMAKE_INSTALL_PREFIX
# so we can't use %%{_datadir} and so forth here.

cmake . -DBUILD_CONFIG=mysql_release \
	-DFEATURE_SET="community" \
	-DINSTALL_LAYOUT=RPM \
	-DCMAKE_INSTALL_PREFIX="%{_prefix}" \
	-DINSTALL_SYSCONFDIR="%{_sysconfdir}" \
	-DINSTALL_INCLUDEDIR=include/mysql \
	-DINSTALL_INFODIR=share/info \
	-DINSTALL_LIBDIR="%{_lib}/mysql" \
	-DINSTALL_MANDIR=share/man \
	-DINSTALL_MYSQLSHAREDIR=share/mysql \
	-DINSTALL_MYSQLTESTDIR=share/mysql-test \
	-DINSTALL_PLUGINDIR="%{_lib}/mysql/plugin" \
	-DINSTALL_SBINDIR=libexec \
	-DINSTALL_SCRIPTDIR=bin \
	-DINSTALL_SQLBENCHDIR=share \
	-DINSTALL_SUPPORTFILESDIR=share/mysql \
	-DMYSQL_DATADIR="%{?_scl_root}/var/lib/mysql" \
	-DMYSQL_UNIX_ADDR="/var/lib/mysql/mysql.sock" \
	-DENABLED_LOCAL_INFILE=ON \
	-DENABLE_DTRACE=ON \
	-DWITH_EMBEDDED_SERVER=ON \
	-DWITH_READLINE=ON \
	-DWITH_SSL=system \
	-DWITH_ZLIB=system \
	-DWITH_MYSQLD_LDFLAGS="-Wl,-z,relro,-z,now"

make %{?_smp_mflags} VERBOSE=1

# debuginfo extraction scripts fail to find source files in their real
# location -- satisfy them by copying these files into location, which
# is expected by scripts
for e in innobase xtradb ; do
  for f in pars0grm.c pars0grm.y pars0lex.l lexyy.c ; do
    cp -p "storage/$e/pars/$f" "storage/$e/$f"
  done
done

%check
%if %runselftest
  # hack to let 32- and 64-bit tests run concurrently on same build machine
  case `uname -m` in
    ppc64 | ppc64p7 | s390x | x86_64 | sparc64 )
      MTR_BUILD_THREAD=7
      ;;
    *)
      MTR_BUILD_THREAD=11
      ;;
  esac
  export MTR_BUILD_THREAD

  make test VERBOSE=1

  # The cmake build scripts don't provide any simple way to control the
  # options for mysql-test-run, so ignore the make target and just call it
  # manually.  Nonstandard options chosen are:
  # --force to continue tests after a failure
  # no retries please
  # test SSL with --ssl
  # skip tests that are listed in rh-skipped-tests.list
  # avoid redundant test runs with --binlog-format=mixed
  # increase timeouts to prevent unwanted failures during mass rebuilds
  (
    cd mysql-test
    perl ./mysql-test-run.pl --force --retry=0 --ssl \
	--skip-test-list=rh-skipped-tests.list \
	--suite-timeout=720 --testcase-timeout=30
    # cmake build scripts will install the var cruft if left alone :-(
    rm -rf var
  ) 
%endif

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

# List the installed tree for RPM package maintenance purposes.
find $RPM_BUILD_ROOT -print | sed "s|^$RPM_BUILD_ROOT||" | sort > ROOTFILES

# multilib header hacks
# we only apply this to known Red Hat multilib arches, per bug #181335
case `uname -i` in
  i386 | x86_64 | ppc | ppc64 | ppc64p7 | s390 | s390x | sparc | sparc64 )
    mv $RPM_BUILD_ROOT%{_includedir}/mysql/my_config.h $RPM_BUILD_ROOT%{_includedir}/mysql/my_config_`uname -i`.h
    mv $RPM_BUILD_ROOT%{_includedir}/mysql/private/config.h $RPM_BUILD_ROOT%{_includedir}/mysql/private/my_config_`uname -i`.h
    install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_includedir}/mysql/
    install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_includedir}/mysql/private/config.h
    ;;
  *)
    ;;
esac

# cmake generates some completely wacko references to -lprobes_mysql when
# building with dtrace support.  Haven't found where to shut that off,
# so resort to this blunt instrument.  While at it, let's not reference
# libmysqlclient_r anymore either.
sed -e 's/-lprobes_mysql//' -e 's/-lmysqlclient_r/-lmysqlclient/' \
	${RPM_BUILD_ROOT}%{_bindir}/mysql_config >mysql_config.tmp
cp -p -f mysql_config.tmp ${RPM_BUILD_ROOT}%{_bindir}/mysql_config
chmod 755 ${RPM_BUILD_ROOT}%{_bindir}/mysql_config

# install INFO_SRC, INFO_BIN into libdir (upstream thinks these are doc files,
# but that's pretty wacko --- see also mariadb-file-contents.patch)
mv ${RPM_BUILD_ROOT}%{_docdir}/mariadb-%{version}/INFO_SRC ${RPM_BUILD_ROOT}%{_libdir}/mysql/
mv ${RPM_BUILD_ROOT}%{_docdir}/mariadb-%{version}/INFO_BIN ${RPM_BUILD_ROOT}%{_libdir}/mysql/

mkdir -p $RPM_BUILD_ROOT/var/log
touch $RPM_BUILD_ROOT/var/log/%{?scl_prefix}mysqld.log

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
# fix path definitions in my.cnf file
sed    -e 's|datadir=/var/|datadir=%{?_scl_root}/var/|g' \
       -e 's|log-error=/var/log/mysqld.log|log-error=/var/log/%{?scl_prefix}mysqld.log|g' \
       -e 's|!includedir /etc/|!includedir %{_sysconfdir}/|g' \
       -e 's|pid-file=/var/|pid-file=%{?_scl_root}/var/|g' >my.cnf <%{SOURCE3}
install -p -m 0644 my.cnf $RPM_BUILD_ROOT%{_sysconfdir}/my.cnf

mkdir -p $RPM_BUILD_ROOT%{?_scl_root}/var/lock/subsys/
mkdir -p $RPM_BUILD_ROOT%{?_scl_root}/var/run/mysqld
install -m 0755 -d $RPM_BUILD_ROOT%{?_scl_root}/var/lib/mysql

# Even if we build for scl, we still create a socket in /var/lib/mysql
%if 0%{?scl:1}
install -m 0755 -d $RPM_BUILD_ROOT/var/lib/mysql
%endif

mkdir -p $RPM_BUILD_ROOT%{?scl:%_root_sysconfdir}%{!?scl:%_sysconfdir}/rc.d/init.d
sed -i -e 's|/etc/my.cnf|%{_sysconfdir}/my.cnf|g' \
       -e 's|/etc/sysconfig/mysqld|%{_sysconfdir}/sysconfig/mysqld|g' \
       -e 's|/etc/sysconfig/\$prog|%{_sysconfdir}/sysconfig/\$prog|g' \
       -e 's|/var/run/mysqld/|%{?_scl_root}/var/run/mysqld/|g' \
       -e 's|/usr|%{_prefix}|g' \
       -e 's|/var/lock/|%{?_scl_root}/var/lock/|g' \
       -e 's|/var/lib/|%{?_scl_root}/var/lib/|g' \
       -e 's|/var/log/mysqld.log|/var/log/%{?scl_prefix}mysqld.log|g' \
       -e 's|get_mysql_option mysqld socket "$datadir/mysql.sock"|get_mysql_option mysqld socket "/var/lib/mysql/mysql.sock"|g' mysql.init
install -p -m 0755 mysql.init $RPM_BUILD_ROOT%{?scl:%_root_sysconfdir}%{!?scl:%_sysconfdir}/rc.d/init.d/%{?scl_prefix}mysqld

# Fix funny permissions that cmake build scripts apply to config files
chmod 644 ${RPM_BUILD_ROOT}%{_datadir}/mysql/config.*.ini

# Fix scripts for multilib safety
mv ${RPM_BUILD_ROOT}%{_bindir}/mysql_config ${RPM_BUILD_ROOT}%{_libdir}/mysql/mysql_config
ln -sf %{_libdir}/mysql/mysql_config ${RPM_BUILD_ROOT}%{_bindir}/mysql_config

mv ${RPM_BUILD_ROOT}%{_bindir}/mysqlbug ${RPM_BUILD_ROOT}%{_libdir}/mysql/mysqlbug
ln -sf %{_libdir}/mysql/mysqlbug ${RPM_BUILD_ROOT}%{_bindir}/mysqlbug

# Remove libmysqld.a
rm -f ${RPM_BUILD_ROOT}%{_libdir}/mysql/libmysqld.a

# libmysqlclient_r is no more.  Upstream tries to replace it with symlinks
# but that really doesn't work (wrong soname in particular).  We'll keep
# just the devel libmysqlclient_r.so link, so that rebuilding without any
# source change is enough to get rid of dependency on libmysqlclient_r.
rm -f ${RPM_BUILD_ROOT}%{_libdir}/mysql/libmysqlclient_r.so*
ln -s libmysqlclient.so ${RPM_BUILD_ROOT}%{_libdir}/mysql/libmysqlclient_r.so
 
# mysql-test includes one executable that doesn't belong under /usr/share,
# so move it and provide a symlink
mv ${RPM_BUILD_ROOT}%{_datadir}/mysql-test/lib/My/SafeProcess/my_safe_process ${RPM_BUILD_ROOT}%{_bindir}
ln -s ../../../../../bin/my_safe_process ${RPM_BUILD_ROOT}%{_datadir}/mysql-test/lib/My/SafeProcess/my_safe_process

# should move this to /etc/ ?
rm -f ${RPM_BUILD_ROOT}%{_bindir}/mysql_embedded
rm -f ${RPM_BUILD_ROOT}%{_libdir}/mysql/*.a
rm -f ${RPM_BUILD_ROOT}%{_datadir}/mysql/binary-configure
rm -f ${RPM_BUILD_ROOT}%{_datadir}/mysql/magic
rm -f ${RPM_BUILD_ROOT}%{_datadir}/mysql/ndb-config-2-node.ini
rm -f ${RPM_BUILD_ROOT}%{_datadir}/mysql/mysql.server
rm -f ${RPM_BUILD_ROOT}%{_datadir}/mysql/mysqld_multi.server
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man1/mysql-stress-test.pl.1*
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man1/mysql-test-run.pl.1*

# put logrotate script where it needs to be
mkdir -p $RPM_BUILD_ROOT%{?scl:%_root_sysconfdir}%{!?scl:%_sysconfdir}/logrotate.d
mv ${RPM_BUILD_ROOT}%{_datadir}/mysql/mysql-log-rotate $RPM_BUILD_ROOT%{?scl:%_root_sysconfdir}%{!?scl:%_sysconfdir}/logrotate.d/%{?scl_prefix}mysqld
chmod 644 $RPM_BUILD_ROOT%{?scl:%_root_sysconfdir}%{!?scl:%_sysconfdir}/logrotate.d/%{?scl_prefix}mysqld

# copy additional docs into build tree so %%doc will find them
cp -p %{SOURCE6} README.mysql-docs
cp -p %{SOURCE7} README.mysql-license
cp -p %{SOURCE18} README.mariadb-devel

# install the list of skipped tests to be available for user runs
install -p -m 0644 mysql-test/rh-skipped-tests.list ${RPM_BUILD_ROOT}%{_datadir}/mysql-test

# we do not provide devel and embeded sub-packages,
# soremove files from that sub-packages
unlink ${RPM_BUILD_ROOT}%{_libdir}/mysql/libmysqld.so
rm -f ${RPM_BUILD_ROOT}%{_libdir}/mysql/libmysqld.so.*
rm -f ${RPM_BUILD_ROOT}%{_bindir}/mysql_client_test_embedded
rm -f ${RPM_BUILD_ROOT}%{_bindir}/mysqltest_embedded
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man1/mysql_client_test_embedded.1*
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man1/mysqltest_embedded.1*

unlink ${RPM_BUILD_ROOT}%{_libdir}/mysql/libmysqlclient.so
unlink ${RPM_BUILD_ROOT}%{_libdir}/mysql/libmysqlclient_r.so
rm -f ${RPM_BUILD_ROOT}%{_libdir}/mysql/libmysqlclient.so.*

# remove unneeded RHEL-4 SELinux stuff
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/mysql/SELinux/

# remove SysV init script
rm -f ${RPM_BUILD_ROOT}%{_sysconfdir}/init.d/mysql

# remove duplicate logrotate script
rm -f ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/mysql

# remove doc files that we rather pack using %%doc
rm -f ${RPM_BUILD_ROOT}%{_datadir}/doc/mariadb-%{version}/COPYING
rm -f ${RPM_BUILD_ROOT}%{_datadir}/doc/mariadb-%{version}/COPYING.LESSER
rm -f ${RPM_BUILD_ROOT}%{_datadir}/doc/mariadb-%{version}/INFO_BIN
rm -f ${RPM_BUILD_ROOT}%{_datadir}/doc/mariadb-%{version}/INFO_SRC
rm -f ${RPM_BUILD_ROOT}%{_datadir}/doc/mariadb-%{version}/INSTALL-BINARY
rm -f ${RPM_BUILD_ROOT}%{_datadir}/doc/mariadb-%{version}/README

# we don't care about scripts for solaris
rm -f ${RPM_BUILD_ROOT}%{_datadir}/mysql/solaris/postinstall-solaris

%clean
rm -rf $RPM_BUILD_ROOT

%pre server
/usr/sbin/groupadd -g 27 -o -r mysql >/dev/null 2>&1 || :
/usr/sbin/useradd -M -N -g mysql -o -r -d /var/lib/mysql -s /bin/bash \
	-c "MariaDB Server" -u 27 mysql >/dev/null 2>&1 || :

%post server
restorecon -R %{_scl_root} >/dev/null 2>&1 || :
restorecon /etc/rc.d/init.d/%{scl_prefix}mysqld >/dev/null 2>&1 || :
if [ $1 = 1 ]; then
    /sbin/chkconfig --add %{?scl_prefix}mysqld
fi
/bin/chmod 0755 %{?_scl_root}/var/lib/mysql
/bin/touch /var/log/%{?scl_prefix}mysqld.log
restorecon /var/log/%{?scl_prefix}mysqld.log >/dev/null 2>&1 || :

%preun server
if [ $1 = 0 ]; then
    /sbin/service %{?scl_prefix}mysqld stop >/dev/null 2>&1
    /sbin/chkconfig --del %{?scl_prefix}mysqld
fi

%postun server
if [ $1 -ge 1 ]; then
    /sbin/service %{?scl_prefix}mysqld condrestart >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root)
%doc README COPYING COPYING.LESSER README.mysql-license
%doc storage/innobase/COPYING.Percona storage/innobase/COPYING.Google
%doc README.mysql-docs

%{_bindir}/msql2mysql
%{_bindir}/mysql
%{_bindir}/mysql_config
%{_bindir}/mysql_find_rows
%{_bindir}/mysql_waitpid
%{_bindir}/mysqlaccess
%{_bindir}/mysqladmin
%{_bindir}/mysqlbinlog
%{_bindir}/mysqlcheck
%{_bindir}/mysqldump
%{_bindir}/mysqlimport
%{_bindir}/mysqlshow
%{_bindir}/mysqlslap
%{_bindir}/my_print_defaults
%{_bindir}/mytop
%{_bindir}/aria_chk
%{_bindir}/aria_dump_log
%{_bindir}/aria_ftdump
%{_bindir}/aria_pack
%{_bindir}/aria_read_log

%{_mandir}/man1/mysql.1*
%{_mandir}/man1/mysql_config.1*
%{_mandir}/man1/mysql_find_rows.1*
%{_mandir}/man1/mysql_waitpid.1*
%{_mandir}/man1/mysqlaccess.1*
%{_mandir}/man1/mysqladmin.1*
%{_mandir}/man1/mysqldump.1*
%{_mandir}/man1/mysqlshow.1*
%{_mandir}/man1/mysqlslap.1*
%{_mandir}/man1/my_print_defaults.1*
%{_mandir}/man1/mysql_fix_privilege_tables.1*
%{_mandir}/man8/mysqlmanager.8*

%{_libdir}/mysql/mysql_config
%config(noreplace) %{_sysconfdir}/my.cnf.d/client.cnf

%files libs
%defattr(-,root,root)
%doc README COPYING COPYING.LESSER README.mysql-license
%doc storage/innobase/COPYING.Percona storage/innobase/COPYING.Google
# although the default my.cnf contains only server settings, we put it in the
# libs package because it can be used for client settings too.
%config(noreplace) %{_sysconfdir}/my.cnf
%config(noreplace) %{_sysconfdir}/my.cnf.d/mysql-clients.cnf
%dir %{_sysconfdir}/my.cnf.d
%dir %{_libdir}/mysql

%dir %{_datadir}/mysql
%{_datadir}/mysql/english
%lang(cs) %{_datadir}/mysql/czech
%lang(da) %{_datadir}/mysql/danish
%lang(nl) %{_datadir}/mysql/dutch
%lang(et) %{_datadir}/mysql/estonian
%lang(fr) %{_datadir}/mysql/french
%lang(de) %{_datadir}/mysql/german
%lang(el) %{_datadir}/mysql/greek
%lang(hu) %{_datadir}/mysql/hungarian
%lang(it) %{_datadir}/mysql/italian
%lang(ja) %{_datadir}/mysql/japanese
%lang(ko) %{_datadir}/mysql/korean
%lang(no) %{_datadir}/mysql/norwegian
%lang(no) %{_datadir}/mysql/norwegian-ny
%lang(pl) %{_datadir}/mysql/polish
%lang(pt) %{_datadir}/mysql/portuguese
%lang(ro) %{_datadir}/mysql/romanian
%lang(ru) %{_datadir}/mysql/russian
%lang(sr) %{_datadir}/mysql/serbian
%lang(sk) %{_datadir}/mysql/slovak
%lang(es) %{_datadir}/mysql/spanish
%lang(sv) %{_datadir}/mysql/swedish
%lang(uk) %{_datadir}/mysql/ukrainian
%{_datadir}/mysql/charsets

%files server
%defattr(-,root,root)
%doc support-files/*.cnf

%{_bindir}/myisamchk
%{_bindir}/myisam_ftdump
%{_bindir}/myisamlog
%{_bindir}/myisampack
%{_bindir}/mysql_convert_table_format
%{_bindir}/mysql_fix_extensions
%{_bindir}/mysql_install_db
%{_bindir}/mysql_plugin
%{_bindir}/mysql_secure_installation
%{_bindir}/mysql_setpermission
%{_bindir}/mysql_tzinfo_to_sql
%{_bindir}/mysql_upgrade
%{_bindir}/mysql_zap
%{_bindir}/mysqlbug
%{_bindir}/mysqldumpslow
%{_bindir}/mysqld_multi
%{_bindir}/mysqld_safe
%{_bindir}/mysqlhotcopy
%{_bindir}/mysqltest
%{_bindir}/innochecksum
%{_bindir}/perror
%{_bindir}/replace
%{_bindir}/resolve_stack_dump
%{_bindir}/resolveip

%config(noreplace) %{_sysconfdir}/my.cnf.d/server.cnf

%{_libexecdir}/mysqld

%{_libdir}/mysql/INFO_SRC
%{_libdir}/mysql/INFO_BIN

%{_libdir}/mysql/mysqlbug

%{_libdir}/mysql/plugin

%{_mandir}/man1/msql2mysql.1*
%{_mandir}/man1/myisamchk.1*
%{_mandir}/man1/myisamlog.1*
%{_mandir}/man1/myisampack.1*
%{_mandir}/man1/mysql_convert_table_format.1*
%{_mandir}/man1/myisam_ftdump.1*
%{_mandir}/man1/mysql.server.1*
%{_mandir}/man1/mysql_fix_extensions.1*
%{_mandir}/man1/mysql_install_db.1*
%{_mandir}/man1/mysql_plugin.1*
%{_mandir}/man1/mysql_secure_installation.1*
%{_mandir}/man1/mysql_upgrade.1*
%{_mandir}/man1/mysql_zap.1*
%{_mandir}/man1/mysqlbug.1*
%{_mandir}/man1/mysqldumpslow.1*
%{_mandir}/man1/mysqlbinlog.1*
%{_mandir}/man1/mysqlcheck.1*
%{_mandir}/man1/mysqld_multi.1*
%{_mandir}/man1/mysqld_safe.1*
%{_mandir}/man1/mysqlhotcopy.1*
%{_mandir}/man1/mysqlimport.1*
%{_mandir}/man1/mysqlman.1*
%{_mandir}/man1/mysql_setpermission.1*
%{_mandir}/man1/mysqltest.1*
%{_mandir}/man1/innochecksum.1*
%{_mandir}/man1/perror.1*
%{_mandir}/man1/replace.1*
%{_mandir}/man1/resolve_stack_dump.1*
%{_mandir}/man1/resolveip.1*
%{_mandir}/man1/mysql_tzinfo_to_sql.1*
%{_mandir}/man8/mysqld.8*

%{_datadir}/mysql/errmsg-utf8.txt
%{_datadir}/mysql/fill_help_tables.sql
%{_datadir}/mysql/mysql_system_tables.sql
%{_datadir}/mysql/mysql_system_tables_data.sql
%{_datadir}/mysql/mysql_test_data_timezone.sql
%{_datadir}/mysql/mysql_performance_tables.sql
%{_datadir}/mysql/my-*.cnf
%{_datadir}/mysql/config.*.ini

%{?scl:%_root_sysconfdir}%{!?scl:%_sysconfdir}/rc.d/init.d/%{?scl_prefix}mysqld

%attr(0755,mysql,mysql) %dir %{?_scl_root}/var/run/mysqld
%attr(0755,mysql,mysql) %dir %{?_scl_root}/var/lib/mysql
%if 0%{?scl:1}
%attr(0755,mysql,mysql) %dir /var/lib/mysql
%endif
%attr(0640,mysql,mysql) %config(noreplace) %verify(not md5 size mtime) /var/log/%{?scl_prefix}mysqld.log
%config(noreplace) %{?scl:%_root_sysconfdir}%{!?scl:%_sysconfdir}/logrotate.d/%{?scl_prefix}mysqld

%files devel
%defattr(-,root,root)
%doc README.mariadb-devel
%{_includedir}/mysql
%{_datadir}/aclocal/mysql.m4
 
%files bench
%defattr(-,root,root)
%{_datadir}/sql-bench

%files test
%defattr(-,root,root)
%{_bindir}/mysql_client_test
%{_bindir}/my_safe_process
%attr(-,mysql,mysql) %{_datadir}/mysql-test

%{_mandir}/man1/mysql_client_test.1*

%changelog
* Fri Jul 19 2013 Honza Horak <hhorak@redhat.com> 5.5.32-1
- Rebase to 5.5.32
  https://kb.askmonty.org/en/mariadb-5532-changelog/

* Mon Jul  1 2013 Honza Horak <hhorak@redhat.com> 5.5.31-3
- Apply fixes found by Coverity static analysis tool
  Resolves: #976765
- Fix misleading error message when uninstalling built-in plugins
  Resolves: #966873

* Tue Jun 11 2013 Honza Horak <hhorak@redhat.com> 5.5.31-2
- Fix service status for unprivileged user
  Resolves: #971776

* Mon Jun 10 2013 Honza Horak <hhorak@redhat.com> 5.5.31-1
- Rebase to 5.5.31
  https://kb.askmonty.org/en/mariadb-5531-changelog/
  Resolves: #966951
- Restore SELinux context of log file
  Resolves: #971380
- Add README.mariadb-devel to document how -devel package should be used
  Resolves: #971808

* Mon May 13 2013 Honza Horak <hhorak@redhat.com> 5.5.30-9
- Run restorecon in %%post section of -server
  Resolves: #962392

* Mon May  6 2013 Honza Horak <hhorak@redhat.com> 5.5.30-7
- Don't try to start daemon if socket file is used already

* Thu May  2 2013 Honza Horak <hhorak@redhat.com> 5.5.30-6
- Fix reporting of service starting
  Resolves: #958098
- Include mysqlhotcopy utility and -devel sub-package for building
  daemon plugins
- Use correct service name in the init script
- Use correct log file path in the logrotate script

* Fri Apr 26 2013 Honza Horak <hhorak@redhat.com> 5.5.30-5
- Remove duplicite directory creation

* Wed Apr 24 2013 Honza Horak <hhorak@redhat.com> 5.5.30-4
- Removing stuff needed for RHEL-7
- Fix checking daemon process status

* Wed Apr 24 2013 Honza Horak <hhorak@redhat.com> 5.5.30-2
- Fix includedir path in my.cnf
- Fix Environment variable name in the init script
- All subpackages should require meta-runtime package
- Preserve timestamps when using install or cp
- Use log file prefixed by scl name and located in /var/log

* Fri Apr  5 2013 Honza Horak <hhorak@redhat.com> 5.5.30-1
- Update to 5.5.30

* Fri Mar 22 2013 Honza Horak <hhorak@redhat.com> 5.5.29-3
- Add specfile pieces for RHEL-5

* Thu Mar 21 2013 Honza Horak <hhorak@redhat.com> 5.5.29-2
- Turn on testing during build

* Thu Mar 21 2013 Honza Horak <hhorak@redhat.com> 5.5.29-1
- Initial packaging for SCL

