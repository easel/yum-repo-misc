%{?scl:%scl_package perl-Test-NoWarnings}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Test-NoWarnings
Version:        1.04
Release:        1%{?dist}
Summary:        Make sure you didn't emit any warnings while testing
License:        LGPLv2+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-NoWarnings/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/Test-NoWarnings-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Devel::StackTrace)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(Test::Builder) >= 0.86
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(Test::Tester) >= 0.107
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
In general, your tests shouldn't produce warnings. This module causes any
warnings to be captured and stored. It automatically adds an extra test
that will run when your script ends to check that there were no warnings.
If there were any warnings, the test will give a "not ok" and diagnostics of
where, when and what the warning was, including a stack trace of what was
going on when the it occurred.

%prep
%setup -q -n Test-NoWarnings-%{version}

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

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-1
- SCL package - initial import
