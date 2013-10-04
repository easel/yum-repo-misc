%{?scl:%scl_package perl-CPAN-Meta-YAML}
%{!?scl:%global pkg_name %{name}}

# We need to patch the test suite if we have Test::More < 0.88
%global old_test_more %(perl -MTest::More -e 'print (($Test::More::VERSION < 0.88) ? 1 : 0);' 2>/dev/null || echo 0)

Name:		%{?scl_prefix}perl-CPAN-Meta-YAML
Version:	0.008
Release:	2%{?dist}
Summary:	Read and write a subset of YAML for CPAN Meta files
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/CPAN-Meta-YAML/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/CPAN-Meta-YAML-%{version}.tar.gz
Patch1:		CPAN-Meta-YAML-0.006-old-Test::More.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
BuildRequires:	%{?scl_prefix}perl(Carp)
BuildRequires:	%{?scl_prefix}perl(Exporter)
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:	%{?scl_prefix}perl(File::Spec)
# Tests:
BuildRequires:	%{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:	%{?scl_prefix}perl(File::Temp)
BuildRequires:	%{?scl_prefix}perl(Test::More)
BuildRequires:	%{?scl_prefix}perl(YAML)
# Don't run extra tests when bootstrapping as many of those
# tests' dependencies build-require this package
%if 0%{!?perl_bootstrap:1}
# RHEL-7 package cannot have buildreqs from EPEL-7 (aspell-en, Pod::Wordlist::hanekomu),
# so skip the spell check there
%if 0%{?rhel} < 7 && ! 0%{?scl:1}
# Version 1.113620 needed for "UTF"
BuildRequires:	%{?scl_prefix}perl(Pod::Wordlist::hanekomu) >= 1.113620
BuildRequires:	%{?scl_prefix}perl(Test::Spelling), aspell-en
%endif
BuildRequires:	%{?scl_prefix}perl(Test::CPAN::Meta)
BuildRequires:	%{?scl_prefix}perl(Test::Pod)
BuildRequires:	%{?scl_prefix}perl(Test::Requires)
# RHEL ≤ 6 doesn't have a recent enough perl(version) for perl(Test::Version) in EPEL
# RHEL ≥ 7 includes this package but does not have perl(Test::Version)
%if 0%{?fedora}
BuildRequires:	%{?scl_prefix}perl(Test::Version)
%endif
%endif
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:	%{?scl_prefix}perl(Carp)
Requires:	%{?scl_prefix}perl(Exporter)

%description
This module implements a subset of the YAML specification for use in reading
and writing CPAN metadata files like META.yml and MYMETA.yml. It should not be
used for any other general YAML parsing or generation task.

%prep
%setup -q -n CPAN-Meta-YAML-%{version}

# We need to patch the test suite if we have Test::More < 0.88
%if %{old_test_more}
%patch1 -p1
%endif

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
rm -rf %{buildroot}
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}
%{?scl:rm -f xt/release/test-version.t xt/author/pod-spell.t}
%if 0%{!?perl_bootstrap:1}
%{?scl:scl enable %{scl} '}
make test TEST_FILES="xt/*/*.t"
%{?scl:'}
%endif

%clean
rm -rf %{buildroot}

%files
%doc Changes LICENSE README
%{perl_vendorlib}/CPAN/
%{_mandir}/man3/CPAN::Meta::YAML.3pm*

%changelog
* Tue Jun 18 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-2
- Update a condition for BRs

* Tue Feb 12 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-1
- Stack package - initial release
