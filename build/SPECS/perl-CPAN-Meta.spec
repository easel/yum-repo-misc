%{?scl:%scl_package perl-CPAN-Meta}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-CPAN-Meta
Summary:        Distribution metadata for a CPAN dist
Version:        2.120921
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/CPAN-Meta-%{version}.tar.gz
URL:            http://search.cpan.org/dist/CPAN-Meta/
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta::YAML) >= 0.008
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Temp) >= 0.20
BuildRequires:  %{?scl_prefix}perl(IO::Dir)
BuildRequires:  %{?scl_prefix}perl(JSON::PP) >= 2.27200
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Parse::CPAN::Meta) >= 1.4403
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.88
BuildRequires:  %{?scl_prefix}perl(version) >= 0.88

# obsolete/provide old tests subpackage
# can be removed during F19 development cycle
Obsoletes:      %{?scl_prefix}%{pkg_name}-tests < 2.113640-3
Provides:       %{?scl_prefix}%{pkg_name}-tests = %{version}-%{release}

%{?perl_default_filter}

%description
Software distributions released to the CPAN include a META.json or, for
older distributions, META.yml, which describes the distribution, its
contents, and the requirements for building and installing the
distribution. The data structure stored in the META.json file is described
in CPAN::Meta::Spec.

%prep
%setup -q -n CPAN-Meta-%{version}

# silence rpmlint warnings
sed -i '1s,#!.*perl,#!%{__perl},' t/*.t

%build
%{?scl:scl enable %{scl} "}
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes history LICENSE README Todo t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Feb  6 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.120921-1
- SCL package - initial release
