%{?scl:%scl_package perl-Test-Pod-Coverage}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Test-Pod-Coverage
Version:        1.08
Release:        1%{?dist}
Summary:        Check for pod coverage in your distribution

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-Pod-Coverage/
Source0:        http://www.cpan.org/authors/id/P/PE/PETDANCE/Test-Pod-Coverage-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(Pod::Coverage)
BuildRequires:  %{?scl_prefix}perl(Test::Builder)
BuildRequires:  %{?scl_prefix}perl(Test::Builder::Tester)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(Test::Pod)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
Checks for POD coverage in files for your distribution.


%prep
%setup -q -n Test-Pod-Coverage-%{version}


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
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3pm*

%changelog
* Wed Feb 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-1
- SCL package - initial import
