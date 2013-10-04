%{?scl:%scl_package perl-IPC-Run3}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-IPC-Run3
Version:        0.045
Release:        1%{?dist}
Summary:        Run a subprocess in batch mode
License:        GPL+ or Artistic or BSD
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IPC-Run3/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/IPC-Run3-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(Getopt::Long)
BuildRequires:  %{?scl_prefix}perl(Test)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.31
BuildRequires:  %{?scl_prefix}perl(Time::HiRes)
# For improved tests
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage)
BuildRequires:  %{?scl_prefix}perl(Test::Pod)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
This module allows you to run a subprocess and redirect stdin, stdout,
and/or stderr to files and perl data structures. It aims to satisfy 99% of
the need for using system, qx, and open3 with a simple, extremely Perlish
API and none of the bloat and rarely used features of IPC::Run.

%prep
%setup -q -n IPC-Run3-%{version}
# Perms in tarballs are broken 
find -type f -exec chmod -x {} \;

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
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Feb 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.045-1
- SCL package - initial import
