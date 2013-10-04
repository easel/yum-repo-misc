%{?scl:%scl_package perl-DBI}
%{!?scl:%global pkg_name %{name}}

# According to documentation, module using Coro is just:
# A PROOF-OF-CONCEPT IMPLEMENTATION FOR EXPERIMENTATION.
%if 0%{?rhel} >= 7 || 0%{?scl:1}
%bcond_with coro
%else
%bcond_without coro
%endif

Name:           %{?scl_prefix}perl-DBI
Version:        1.627
Release:        1%{?dist}
Summary:        A database access API for perl
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://dbi.perl.org/
Source0:        http://www.cpan.org/authors/id/T/TI/TIMB/DBI-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Carp)
# Clone is optional
BuildRequires:  %{?scl_prefix}perl(Clone) >= 0.34
BuildRequires:  %{?scl_prefix}perl(Config)
%if %{with coro}
BuildRequires:  %{?scl_prefix}perl(Coro)
BuildRequires:  %{?scl_prefix}perl(Coro::Handle)
BuildRequires:  %{?scl_prefix}perl(Coro::Select)
%endif
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
# DB_File is optional
BuildRequires:  %{?scl_prefix}perl(DB_File)
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(Errno)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Fcntl)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(Getopt::Long)
BuildRequires:  %{?scl_prefix}perl(IO::Dir)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(IO::Select)
BuildRequires:  %{?scl_prefix}perl(IPC::Open3)
BuildRequires:  %{?scl_prefix}perl(Math::BigInt)
# MLDBM is optional
%if ! ( 0%{?rhel} )
BuildRequires:  %{?scl_prefix}perl(MLDBM)
%endif
# Params::Util is optional
# RPC::PlClient is optional
BuildRequires:  %{?scl_prefix}perl(RPC::PlClient) >= 0.2000
# RPC::PlServer is optional
BuildRequires:  %{?scl_prefix}perl(RPC::PlServer)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
# SQL::Statement is optional, and it requires DBI
%if 0%{!?perl_bootstrap:1} && ! ( 0%{?rhel} )
BuildRequires:  %{?scl_prefix}perl(SQL::Statement) >= 1.402
%endif
BuildRequires:  %{?scl_prefix}perl(Storable)
BuildRequires:  %{?scl_prefix}perl(Symbol)
BuildRequires:  %{?scl_prefix}perl(threads)
BuildRequires:  %{?scl_prefix}perl(Tie::Hash)
BuildRequires:  %{?scl_prefix}perl(UNIVERSAL)
BuildRequires:  %{?scl_prefix}perl(utf8)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests
BuildRequires:  %{?scl_prefix}perl(Benchmark)
BuildRequires:  %{?scl_prefix}perl(Encode)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Net::Daemon::Test)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(Test::Simple) >= 0.90
# Optional tests
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.00
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage) >= 1.04
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version') }
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(Math::BigInt)

# Filter unwanted dependencies
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}perl\\(RPC::\\)

%description 
DBI is a database access Application Programming Interface (API) for
the Perl Language. The DBI API Specification defines a set of
functions, variables and conventions that provide a consistent
database interface independent of the actual database being used.

%prep
%setup -q -n DBI-%{version} 
iconv -f iso8859-1 -t utf-8 lib/DBD/Gofer.pm >lib/DBD/Gofer.pm.new &&
  mv lib/DBD/Gofer.pm{.new,}
chmod 644 ex/*
chmod 744 dbixs_rev.pl
sed -i 's?#!perl?#!%{__perl}?' ex/corogofer.pl
%if %{without coro}
rm lib/DBD/Gofer/Transport/corostream.pm
sed -i -e '/^lib\/DBD\/Gofer\/Transport\/corostream.pm$/d' MANIFEST
%endif

%build
%{?scl:scl enable %{scl} '}
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{?scl:'}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*
# Remove Win32 specific files and man pages to avoid unwanted dependencies
rm -rf %{buildroot}%{perl_vendorarch}/{Win32,DBI/W32ODBC.pm} \
    %{buildroot}%{_mandir}/man3/{DBI::W32,Win32::DBI}ODBC.3pm
%{?scl:scl enable %{scl} - << \EOF}
perl -pi -e 's"#!perl -w"#!/usr/bin/perl -w"' \
    %{buildroot}%{perl_vendorarch}/{goferperf,dbixs_rev}.pl
%{?scl:EOF}

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
# Changes already packaged as DBI::Changes
%doc README.md ex/
%{_bindir}/dbipro*
%{_bindir}/dbilogstrip
%{perl_vendorarch}/*.p*
%{perl_vendorarch}/Bundle/
%{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBI/
%{perl_vendorarch}/auto/DBI/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%changelog
* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.627-1
- 1.627 bump

* Tue Mar 12 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.623-1
- SCL package - initial import
