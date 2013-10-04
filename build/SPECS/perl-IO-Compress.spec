%{?scl:%scl_package perl-IO-Compress}
%{!?scl:%global pkg_name %{name}}

%bcond_without long_tests
%{?perl_default_filter}

Name:           %{?scl_prefix}perl-IO-Compress
Version:        2.060
Release:        1%{?dist}
Summary:        Read and write compressed data
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IO-Compress/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/IO-Compress-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Compress::Raw::Bzip2) >= %{version}
BuildRequires:  %{?scl_prefix}perl(Compress::Raw::Zlib) >= %{version}
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Encode)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(IO::Seekable)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(List::Util)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
# Dual-lived module needs building early in the boot process
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(Test::NoWarnings)
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.00
%endif
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
# this is wrapper for different Compress modules
Obsoletes:      %{?scl_prefix}perl-Compress-Zlib < %{version}-%{release}
Provides:       %{?scl_prefix}perl-Compress-Zlib = %{version}-%{release}
Obsoletes:      %{?scl_prefix}perl-IO-Compress-Base < %{version}-%{release}
Provides:       %{?scl_prefix}perl-IO-Compress-Base = %{version}-%{release}
Obsoletes:      %{?scl_prefix}perl-IO-Compress-Bzip2 < %{version}-%{release}
Provides:       %{?scl_prefix}perl-IO-Compress-Bzip2 = %{version}-%{release}
Obsoletes:      %{?scl_prefix}perl-IO-Compress-Zlib < %{version}-%{release}
Provides:       %{?scl_prefix}perl-IO-Compress-Zlib = %{version}-%{release}

%description
This distribution provides a Perl interface to allow reading and writing of
compressed data created with the zlib and bzip2 libraries.

IO-Compress supports reading and writing of bzip2, RFC 1950, RFC 1951,
RFC 1952 (i.e. gzip) and zip files/buffers.

The following modules used to be distributed separately, but are now
included with the IO-Compress distribution:
* Compress-Zlib
* IO-Compress-Zlib
* IO-Compress-Bzip2
* IO-Compress-Base

%prep
%setup -q -n IO-Compress-%{version}

# Remove spurious exec permissions
chmod -c -x lib/IO/Uncompress/{Adapter/Identity,RawInflate}.pm
find examples -type f -exec chmod -c -x {} \;

# Fix shellbangs in examples
%{?scl:scl enable %{scl} "}
perl -pi -e 's|^#!/usr/local/bin/perl\b|#!%{__perl}|' examples/io/anycat \
        examples/io/bzip2/* examples/io/gzip/* examples/compress-zlib/*
%{?scl:"}

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot} INSTALLDIRS=perl
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%check
# Build using "--without long_tests" to avoid very long tests
# (full suite can take nearly an hour on an i7)
%{?scl:scl enable %{scl} "}
make test %{?with_long_tests:COMPRESS_ZLIB_RUN_ALL=1}
%{?scl:"}

%files
%doc Changes README examples/*
%{_bindir}/zipdetails
%{perl_privlib}/Compress/
%{perl_privlib}/File/
%dir %{perl_privlib}/IO/
%dir %{perl_privlib}/IO/Compress/
%doc %{perl_privlib}/IO/Compress/FAQ.pod
%{perl_privlib}/IO/Compress/Adapter/
%{perl_privlib}/IO/Compress/Base/
%{perl_privlib}/IO/Compress/Base.pm
%{perl_privlib}/IO/Compress/Bzip2.pm
%{perl_privlib}/IO/Compress/Deflate.pm
%{perl_privlib}/IO/Compress/Gzip/
%{perl_privlib}/IO/Compress/Gzip.pm
%{perl_privlib}/IO/Compress/RawDeflate.pm
%{perl_privlib}/IO/Compress/Zip/
%{perl_privlib}/IO/Compress/Zip.pm
%{perl_privlib}/IO/Compress/Zlib/
%{perl_privlib}/IO/Uncompress/
%{_mandir}/man1/zipdetails.1*
%{_mandir}/man3/Compress::Zlib.3pm*
%{_mandir}/man3/File::GlobMapper.3pm*
%{_mandir}/man3/IO::Compress::*.3pm*
%{_mandir}/man3/IO::Uncompress::*.3pm*

%changelog
* Tue Feb 12 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.060-1
- SCL package - initial import
