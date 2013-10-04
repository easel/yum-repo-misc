%{?scl:%scl_package perl-CPAN-Meta-Requirements}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-CPAN-Meta-Requirements
Version:        2.122
Release:        1%{?dist}
Summary:        Set of version requirements for a CPAN dist
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CPAN-Meta-Requirements/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/CPAN-Meta-Requirements-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(Test::Script)
%endif
BuildRequires:  %{?scl_prefix}perl(version) >= 0.77
# for author/release tests
%if !%{defined perl_bootstrap} && ! ( 0%{?rhel} )
BuildRequires:  %{?scl_prefix}perl(Perl::Critic::Policy::Lax::ProhibitStringyEval::ExceptForRequire)
BuildRequires:  %{?scl_prefix}perl(Pod::Coverage::TrustPod)
BuildRequires:  %{?scl_prefix}perl(Pod::Wordlist::hanekomu)
BuildRequires:  %{?scl_prefix}perl(Test::CPAN::Meta)
BuildRequires:  %{?scl_prefix}perl(Test::Perl::Critic)
BuildRequires:  %{?scl_prefix}perl(Test::Pod)
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage)
BuildRequires:  %{?scl_prefix}perl(Test::Portability::Files)
BuildRequires:  %{?scl_prefix}perl(Test::Requires)
BuildRequires:  %{?scl_prefix}perl(Test::Spelling), aspell-en
BuildRequires:  %{?scl_prefix}perl(Test::Version)
%endif

%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%{?perl_default_filter}
%{?scl:
%filter_from_provides /perl(CPAN::Meta::Requirements)/d
%filter_setup
}

# CPAN-Meta-Requirements was split from CPAN-Meta
Conflicts:      %{?scl_prefix}perl-CPAN-Meta < 2.120921
# and used to have six decimal places
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(CPAN::Meta::Requirements\\)
Provides:       %{?scl_prefix}perl(CPAN::Meta::Requirements) = %{version}000

%description
A CPAN::Meta::Requirements object models a set of version constraints like
those specified in the META.yml or META.json files in CPAN distributions.
It can be built up by adding more and more constraints, and it will reduce
them to the simplest representation.

%prep
%setup -q -n CPAN-Meta-Requirements-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
%if %{defined perl_bootstrap} || ( 0%{?rhel} )
rm -rf xt
%endif
%{?scl:scl enable %{scl} '}
make test TEST_FILES="t/*.t xt/*/*.t"
%{?scl:'}

%files
%doc Changes LICENSE perlcritic.rc README README.PATCHING
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Feb  6 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.122-1
- Stack package - initial release
