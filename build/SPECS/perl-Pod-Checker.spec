%{?scl:%scl_package perl-Pod-Checker}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Pod-Checker
Version:        1.60
Release:        1%{?dist}
Summary:        Check POD documents for syntax errors
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Pod-Checker/
Source0:        http://www.cpan.org/authors/id/M/MA/MAREKR/Pod-Checker-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Pod::Parser) >= 1.60
BuildRequires:  %{?scl_prefix}perl(Pod::ParseUtils)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
# Tests:
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(FileHandle)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(Pod::Parser) >= 1.60

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Pod::Parser\\)$

%{?scl:
%filter_from_requires /perl(Pod::Parser)\s*$/d
%filter_setup
}

%description
Module and tools to verify POD documentation contents for compliance with the
Plain Old Documentation format specifications.

%prep
%setup -q -n Pod-Checker-%{version}
find -type f -exec chmod a-x {} +
for F in CHANGES README; do
    sed -i -e 's/\r//' "$F"
done

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc CHANGES README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Feb 18 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.60-1
- SCL package - initial import
