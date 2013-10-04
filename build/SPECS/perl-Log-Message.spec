%{?scl:%scl_package perl-Log-Message}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Log-Message
# Epoch to compete with perl.spec
Epoch:          1
Version:        0.08
Release:        1%{?dist}
Summary:        Generic message storing mechanism
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Log-Message/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/Log-Message-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
%if 0%(perl -e 'print $] > 5.017')
BuildRequires:  %{?scl_prefix}perl(deprecate)
%endif
BuildRequires:  %{?scl_prefix}perl(FileHandle)
BuildRequires:  %{?scl_prefix}perl(if)
BuildRequires:  %{?scl_prefix}perl(Locale::Maketext::Simple)
BuildRequires:  %{?scl_prefix}perl(Module::Load)
BuildRequires:  %{?scl_prefix}perl(Params::Check)
BuildRequires:  %{?scl_prefix}perl(vars)
# Tests:
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
%if 0%(perl -e 'print $] > 5.017')
Requires:       %{?scl_prefix}perl(deprecate)
%endif

%description
This package enables you to do generic message logging throughout programs and
projects. Every message will be logged with stack traces, time stamps and so
on.  You can use built-in handlers immediately, or after the fact when you
inspect the error stack. It is highly configurable and let's you even provide
your own handlers for dealing with messages.

%prep
%setup -q -n Log-Message-%{version}

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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.08-1
- 0.08 bump, correct a typo in dependencies

* Fri Feb 15 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.06-1
- SCL package - initial import
