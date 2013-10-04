%{?scl:%scl_package perl-Parse-CPAN-Meta}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Parse-CPAN-Meta
# dual-lifed module needs to match the epoch in perl.spec
Epoch:          1
Version:        1.4404
Release:        1%{?dist}
Summary:        Parse META.yml and META.json CPAN meta-data files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Parse-CPAN-Meta/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/Parse-CPAN-Meta-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta::YAML) >= 0.008
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.80
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(JSON::PP) >= 2.27200
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.47
Requires:       %{?scl_prefix}perl(CPAN::Meta::YAML) >= 0.008
Requires:       %{?scl_prefix}perl(Exporter)
Requires:       %{?scl_prefix}perl(JSON::PP) >= 2.27200
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%{?perl_default_filter}

%description
Parse::CPAN::Meta is a parser for META.json and META.yml files, using
JSON::PP and/or CPAN::Meta::YAML.

%prep
%setup -q -n Parse-CPAN-Meta-%{version}

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
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Feb  6 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4404-1
- Stack package - initial release
