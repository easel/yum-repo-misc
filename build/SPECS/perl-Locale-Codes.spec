%{?scl:%scl_package perl-Locale-Codes}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Locale-Codes
Version:        3.25
Release:        1%{?dist}
Summary:        Distribution of modules to handle locale codes
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Locale-Codes/
Source0:        http://www.cpan.org/authors/id/S/SB/SBECK/Locale-Codes-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
# Tests
BuildRequires:  %{?scl_prefix}perl(Storable)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

# Inject not detected module version
%{?filter_setup:
%filter_from_provides s/\(perl(Locale\>[^)]*)\)[^=]*$/\1 = %{version}/
%filter_setup
}

%description
Locale-Codes is a distribution containing a set of modules. The modules
each deal with different types of codes which identify parts of the locale
including languages, countries, currency, etc.

%prep
%setup -q -n Locale-Codes-%{version}
chmod -x examples/*

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
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc ChangeLog LICENSE README README.first examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3.25-1
- 3.25 bump

* Wed Feb 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3.24-1
- SCL package - initial import
