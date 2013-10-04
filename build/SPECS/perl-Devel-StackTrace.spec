%{?scl:%scl_package perl-Devel-StackTrace}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Devel-StackTrace
Summary:        Perl module implementing stack trace and stack trace frame objects
Version:        1.30
Epoch:          1
Release:        1%{?dist}
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-StackTrace/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Devel-StackTrace-%{version}.tar.gz
BuildArch:      noarch

# --with release_tests ... also check "RELEASE_TESTS".
# Disabled by default
%bcond_with release_tests

BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.88
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%if %{with release_tests}
# for improved tests
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(bytes)
BuildRequires:  %{?scl_prefix}perl(Exception::Class::Base)
BuildRequires:  %{?scl_prefix}perl(Test::Pod)
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  %{?scl_prefix}perl(Test::EOL)
BuildRequires:  %{?scl_prefix}perl(Test::NoTabs)
BuildRequires:  %{?scl_prefix}perl(Test::Spelling)
BuildRequires:  %{?scl_prefix}perl(Test::CPAN::Changes)
BuildRequires:  %{?scl_prefix}perl(Test::Pod::LinkCheck)
BuildRequires:  %{?scl_prefix}perl(Test::Pod::No404s)
BuildRequires:  %{?scl_prefix}perl(LWP::Protocol::https)
BuildRequires:  aspell-en
%endif

%description
The Devel::StackTrace module contains two classes, Devel::StackTrace
and Devel::StackTraceFrame.  The goal of this object is to encapsulate
the information that can found through using the caller() function, as
well as providing a simple interface to this data.

The Devel::StackTrace object contains a set of Devel::StackTraceFrame
objects, one for each level of the stack.  The frames contain all the
data available from caller() as of Perl 5.6.0.

%prep
%setup -q -n Devel-StackTrace-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{?scl:"}

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test %{?with_release_tests:RELEASE_TESTING=1}
%{?scl:"}

%files
%doc README LICENSE Changes
%{perl_vendorlib}/Devel
%{_mandir}/man3/*

%changelog
* Thu Feb 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.30-1
- SCL package - initial import
