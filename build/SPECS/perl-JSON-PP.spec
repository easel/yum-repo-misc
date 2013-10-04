%{?scl:%scl_package perl-JSON-PP}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}perl-JSON-PP
Version:	2.27202
Release:	100%{?dist}
Summary:	JSON::XS compatible pure-Perl module
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/JSON-PP/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MAKAMAKA/JSON-PP-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
BuildRequires:	%{?scl_prefix}perl(base)
BuildRequires:	%{?scl_prefix}perl(Carp)
BuildRequires:	%{?scl_prefix}perl(constant)
BuildRequires:	%{?scl_prefix}perl(Data::Dumper)
BuildRequires:	%{?scl_prefix}perl(Encode)
BuildRequires:	%{?scl_prefix}perl(Exporter)
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:	%{?scl_prefix}perl(lib)
BuildRequires:	%{?scl_prefix}perl(Math::BigFloat)
BuildRequires:	%{?scl_prefix}perl(Math::BigInt)
BuildRequires:	%{?scl_prefix}perl(Test::More)
BuildRequires:	%{?scl_prefix}perl(Tie::IxHash)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:	%{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:	%{?scl_prefix}perl(Data::Dumper)
Conflicts:	%{?scl_prefix}perl-JSON < 2.50

%description
JSON::XS is the fastest and most proper JSON module on CPAN. It is written by
Marc Lehmann in C, so must be compiled and installed in the used environment.

JSON::PP is a pure-Perl module and is compatible with JSON::XS.

%prep
%setup -q -n JSON-PP-%{version}

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

%clean
rm -rf %{buildroot}

%files
%doc Changes README
%{_bindir}/json_pp
%{perl_vendorlib}/JSON/
%{_mandir}/man1/json_pp.1*
%{_mandir}/man3/JSON::PP.3pm*
%{_mandir}/man3/JSON::PP::Boolean.3pm*

%changelog
* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.27202-1
- 2.27202 bump

* Thu Feb 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.27200-100
- SCL package - initial import
