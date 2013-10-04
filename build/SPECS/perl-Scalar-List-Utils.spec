%{?scl:%scl_package perl-Scalar-List-Utils}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Scalar-List-Utils
Version:        1.27
Release:        100%{?dist}
Summary:        A selection of general-utility scalar and list subroutines
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Scalar-List-Utils/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/Scalar-List-Utils-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(Math::BigInt)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Symbol)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(Tie::Handle)
BuildRequires:  %{?scl_prefix}perl(Tie::Scalar)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(Carp)

%{?perl_default_filter}

%{?scl:
%filter_from_provides /\.so()/d
%filter_setup
}

%description
This package contains a selection of subroutines that people have expressed
would be nice to have in the perl core, but the usage would not really be
high enough to warrant the use of a keyword, and the size so small such
that being individual extensions would be wasteful.

%prep
%setup -q -n Scalar-List-Utils-%{version}

%build
%{?scl:scl enable %{scl} '}
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/List*
%{perl_vendorarch}/Scalar*
%{_mandir}/man3/*

%changelog
* Wed Feb 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-100
- SCL package - initial import
