%{?scl:%scl_package perl-Test-CPAN-Meta}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Test-CPAN-Meta
Version:        0.23
Release:        1%{?dist}
Summary:        Validation of the META.yml file in a CPAN distribution
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-CPAN-Meta/
Source0:        http://www.cpan.org/authors/id/B/BA/BARBIE/Test-CPAN-Meta-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(id -nu)
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(Parse::CPAN::Meta) >= 0.02
BuildRequires:  %{?scl_prefix}perl(Test::Builder)
BuildRequires:  %{?scl_prefix}perl(Test::Builder::Tester)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.70
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.00
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage) >= 0.08
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
This module was written to ensure that a META.yml file, provided with a
standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of package makers
and installers such as ExtUtils::MakeMaker, Module::Build and
Module::Install.

%prep
%setup -q -n Test-CPAN-Meta-%{version}

iconv -f iso-8859-1 -t utf-8 LICENSE > LICENSE.tmp
mv -f LICENSE.tmp LICENSE

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
rm -rf $RPM_BUILD_ROOT

%{?scl:scl enable %{scl} "}
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{?scl:"}

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT

%check
%{?scl:scl enable %{scl} "}
make test AUTOMATED_TESTING=1
%{?scl:"}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README examples/
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::CPAN::Meta.3pm*
%{_mandir}/man3/Test::CPAN::Meta::Version.3pm*

%changelog
* Tue May 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-1
- 0.23 bump

* Thu Feb 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-1
- SCL package - initial import
