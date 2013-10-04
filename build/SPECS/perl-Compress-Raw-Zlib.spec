%{?scl:%scl_package perl-Compress-Raw-Zlib}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Compress-Raw-Zlib
Version:        2.060
Release:        1%{?dist}
Summary:        Low-level interface to the zlib compression library
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Compress-Raw-Zlib/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/Compress-Raw-Zlib-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}perl(AutoLoader)
# XSLoader or DynaLoader; choose wisely
BuildRequires:  %{?scl_prefix}perl(XSLoader)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Dual-lived module needs rebuilding early in the boot process
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(Test::NoWarnings)
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.00
%endif
BuildRequires:  zlib-devel
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
# see above
Requires:       %{?scl_prefix}perl(XSLoader)

%{?scl:
%filter_from_provides /\.so()/d
%filter_setup
}

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
The Compress::Raw::Zlib module provides a Perl interface to the zlib
compression library, which is used by IO::Compress::Zlib.

%prep
%setup -q -n Compress-Raw-Zlib-%{version}

%build
BUILD_ZLIB=False 
OLD_ZLIB=False
ZLIB_LIB=%{_libdir}
ZLIB_INCLUDE=%{_includedir}
export BUILD_ZLIB OLD_ZLIB ZLIB_LIB ZLIB_INCLUDE

%{?scl:scl enable %{scl} '}
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{?scl:'}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes README
%{perl_vendorarch}/auto/Compress/
%{perl_vendorarch}/Compress/
%{_mandir}/man3/Compress::Raw::Zlib.3pm*

%changelog
* Tue Feb 12 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.060-1
- Stack package - initial release
