%{?scl:%scl_package perl-Version-Requirements}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Version-Requirements
Version:        0.101022
Release:        100%{?dist}
Summary:        Set of version requirements for a CPAN dist (DEPRECATED)
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Version-Requirements/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Version-Requirements-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.30
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
# tests
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.88
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.41
%endif
BuildRequires:  %{?scl_prefix}perl(version) >= 0.77
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%{?perl_default_filter}

#%%{?scl:
#%%filter_from_provides /\.so()/d
#%%filter_setup
#}

%description
Version::Requirements is now DEPRECATED.

Use CPAN::Meta::Requirements, which is a drop-in replacement.

A Version::Requirements object models a set of version constraints like
those specified in the META.yml or META.json files in CPAN distributions.
It can be built up by adding more and more constraints, and it will reduce
them to the simplest representation.

%prep
%setup -q -n Version-Requirements-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
rm -rf $RPM_BUILD_ROOT

%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Feb 19 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.101022-100
- SCL package - initial import
