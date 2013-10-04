%{?scl:%scl_package perl-Thread-Queue}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Thread-Queue
Version:        3.02
Release:        1%{?dist}
Summary:        Thread-safe queues
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Thread-Queue/
Source0:        http://www.cpan.org/authors/id/J/JD/JDHEDDEN/Thread-Queue-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util) >= 1.10
BuildRequires:  %{?scl_prefix}perl(threads::shared) >= 1.21
# Tests:
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.50
BuildRequires:  %{?scl_prefix}perl(Thread::Semaphore)
BuildRequires:  %{?scl_prefix}perl(threads)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(Carp)

%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}%{_datadir}/doc/

%{?scl:
%filter_from_requires /%{_datadir}\/doc\//
%filter_setup
}

%description
This module provides thread-safe FIFO queues that can be accessed safely by
any number of threads.

%prep
%setup -q -n Thread-Queue-%{version}

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
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Apr 04 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3.02-1
- SCL package - initial import
