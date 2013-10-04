%{?scl:%scl_package perl-Probe-Perl}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Probe-Perl
Version:        0.02
Release:        1%{?dist}
Summary:        Information about the currently running perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Probe-Perl/
Source0:        http://www.cpan.org/authors/id/K/KW/KWILLIAMS/Probe-Perl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
# Tests:
BuildRequires:  %{?scl_prefix}perl(English)
BuildRequires:  %{?scl_prefix}perl(Test)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
This module provides methods for obtaining information about the currently
running perl interpreter. It originally began life as code in the
Module::Build project, but has been externalized here for general use.

%prep
%setup -q -n Probe-Perl-%{version}

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue May 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-1
- 0.02 bump

* Wed Feb 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.01-1
- SCL package - initial import
