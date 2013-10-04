%{?scl:%scl_package perl-Test-Script}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Test-Script
Version:        1.07
Release:        2%{?dist}
Summary:        Cross-platform basic tests for scripts
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Script/
Source0:        http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Test-Script-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(File::Spec::Unix)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(IPC::Run3) >= 0.034
BuildRequires:  %{?scl_prefix}perl(Probe::Perl)
BuildRequires:  %{?scl_prefix}perl(Test::Builder)
BuildRequires:  %{?scl_prefix}perl(Test::Builder::Tester)
BuildRequires:  %{?scl_prefix}perl(Test::More)

# For improved tests
%if !%{defined perl_bootstrap} && ! 0%{?scl:1}
BuildRequires:  %{?scl_prefix}perl(Test::CPAN::Meta) >= 0.12
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.26
BuildRequires:  %{?scl_prefix}perl(Test::MinimumVersion) >= 0.008
BuildRequires:  %{?scl_prefix}perl(Perl::MinimumVersion) >= 1.20
BuildRequires:  %{?scl_prefix}perl(Pod::Simple) >= 3.07
%endif
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
The intent of this module is to provide a series of basic tests for scripts
in the bin directory of your Perl distribution.

%prep
%setup -q -n Test-Script-%{version}

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

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if !%{defined perl_bootstrap} && ! 0%{?scl:1}
%{?scl:scl enable %{scl} "}
make test AUTOMATED_TESTING=1 RELEASE_TESTING=1
%{?scl:"}
%else 
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 18 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-2
- Update a condition for BRs

* Wed Feb 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-1
- SCL package - initial import
