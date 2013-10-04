%{?scl:%scl_package perl-Compress-Raw-Bzip2}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Compress-Raw-Bzip2
Summary:        Low-level interface to bzip2 compression library
Version:        2.060
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Compress-Raw-Bzip2/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/Compress-Raw-Bzip2-%{version}.tar.gz 
BuildRequires:  bzip2-devel
BuildRequires:  %{?scl_prefix}perl(AutoLoader)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(Test::Pod)
%endif
# XSLoader or DynaLoader; choose wisely
BuildRequires:  %{?scl_prefix}perl(XSLoader)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
# see above
Requires:       %{?scl_prefix}perl(XSLoader)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%{?scl:
%filter_from_provides /\.so()/d
%filter_setup
}


%description
This module provides a Perl interface to the bzip2 compression library.
It is used by IO::Compress::Bzip2.

%prep
%setup -q -n Compress-Raw-Bzip2-%{version}

%build
BUILD_BZIP2=0
BZIP2_LIB=%{_libdir}
export BUILD_BZIP2 BZIP2_LIB

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
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes README
%{perl_vendorarch}/auto/Compress/
%{perl_vendorarch}/Compress/
%{_mandir}/man3/Compress::Raw::Bzip2.3pm*

%changelog
* Wed Feb  6 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.060-1
- Stack package - initial release
