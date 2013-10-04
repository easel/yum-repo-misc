%{?scl:%scl_package perl-Module-Metadata}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}perl-Module-Metadata
Version:	1.000016
Release:	1%{?dist}
Summary:	Gather package and POD information from perl module files
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Module-Metadata/
Source0:	http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/Module-Metadata-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
# Module
BuildRequires:	%{?scl_prefix}perl(Carp)
BuildRequires:	%{?scl_prefix}perl(File::Find)
BuildRequires:	%{?scl_prefix}perl(File::Spec)
BuildRequires:	%{?scl_prefix}perl(IO::File)
BuildRequires:	%{?scl_prefix}perl(strict)
BuildRequires:	%{?scl_prefix}perl(vars)
BuildRequires:	%{?scl_prefix}perl(version) >= 0.87
BuildRequires:	%{?scl_prefix}perl(warnings)
# Regular test suite
BuildRequires:	%{?scl_prefix}perl(Cwd)
BuildRequires:	%{?scl_prefix}perl(Data::Dumper)
BuildRequires:	%{?scl_prefix}perl(Exporter)
BuildRequires:	%{?scl_prefix}perl(File::Temp)
BuildRequires:	%{?scl_prefix}perl(File::Path)
BuildRequires:	%{?scl_prefix}perl(lib)
BuildRequires:	%{?scl_prefix}perl(Test::More)
# Release tests
%if !%{defined perl_bootstrap}
BuildRequires:	%{?scl_prefix}perl(Test::Pod)
BuildRequires:	%{?scl_prefix}perl(Test::Pod::Coverage)
%endif
# Runtime
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:	%{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
This module provides a standard way to gather metadata about a .pm file
without executing unsafe code.

%prep
%setup -q -n Module-Metadata-%{version}

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}
%if !%{defined perl_bootstrap}
%{?scl:scl enable %{scl} '}
make test TEST_FILES="xt/*.t"
%{?scl:'}
%endif

%files
%doc Changes README
%{perl_vendorlib}/Module/
%{_mandir}/man3/Module::Metadata.3pm*

%changelog
* Fri Aug 23 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.000016-1
- Update to 1.000016
- Resolves: rhbz#996286 - Change wording about safety/security to satisfy
  CVE-2013-1437
- Update source URL
- Specify all dependencies

* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.000014-1
- 1.000014 bump

* Wed Feb 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.000011-1
- SCL package - initial import
