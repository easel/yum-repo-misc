%{?scl:%scl_package perl-%{cpan_name}}
%{!?scl:%global pkg_name %{name}}

%global cpan_name ExtUtils-MakeMaker
%global cpan_version 6.66

Name:           %{?scl_prefix}perl-%{cpan_name}
Version:        %(echo '%{cpan_version}' | tr _ .)
Release:        1%{?dist}
Summary:        Create a module Makefile
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/%{cpan_name}/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{cpan_version}.tar.gz
# Do not set RPATH to perl shared-library modules by default. Bug #773622.
# This is copy from `perl' package. This is distributor extension.
Patch0:         %{cpan_name}-6.64-USE_MM_LD_RUN_PATH.patch
BuildArch:      noarch
# Makefile.Pl uses ExtUtils::MakeMaker from ./lib
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.8
BuildRequires:  %{?scl_prefix}perl(lib)
# Unbundled
BuildRequires:  %{?scl_prefix}perl(File::Copy::Recursive)
# Tests:
BuildRequires:  %{?scl_prefix}perl(AutoSplit)
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Command)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Install)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Installed)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Manifest)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(Getopt::Long)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Parse::CPAN::Meta)
BuildRequires:  %{?scl_prefix}perl(Pod::Man)
BuildRequires:  %{?scl_prefix}perl(Test::Harness)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Optional tests
BuildRequires:  %{?scl_prefix}perl(ExtUtils::CBuilder)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(ExtUtils::Command)
Requires:       %{?scl_prefix}perl(ExtUtils::Install)
Requires:       %{?scl_prefix}perl(ExtUtils::Manifest)
Requires:       %{?scl_prefix}perl(File::Find)
Requires:       %{?scl_prefix}perl(File::Spec) >= 0.8
Requires:       %{?scl_prefix}perl(Getopt::Long)
Requires:       %{?scl_prefix}perl(Test::Harness)
# Optional run-time needed for generating documentation from POD:
Requires:       %{?scl_prefix}perl(Pod::Man)

# Do not export underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)\s*$
# Do not export private redefinitions
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DynaLoader|ExtUtils::MakeMaker::_version\\)

%{?scl:
%filter_from_requires /perl(File::Spec)\s*$/
%filter_from_provides /perl(\(DynaLoader\|ExtUtils::MakeMaker::_version\))/d
%filter_setup
}

%description
This utility is designed to write a Makefile for an extension module from a
Makefile.PL. It is based on the Makefile.SH model provided by Andy
Dougherty and the perl5-porters.

%prep
%setup -q -n ExtUtils-MakeMaker-%{cpan_version}
%patch0 -p1
# Remove bundled modules
rm -rf bundled/* ||:
sed -i -e '/^bundled\// d' MANIFEST

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
%doc Changes NOTES PATCHING README TODO
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 6.66-1
- 6.66 bump

* Fri Feb  8 2013 Jitka Plesnikova <jplesnik@redhat.com> - 6.64-1
- SCL package - initial release
