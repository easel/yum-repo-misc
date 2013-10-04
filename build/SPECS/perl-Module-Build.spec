%{?scl:%scl_package perl-Module-Build}
%{!?scl:%global pkg_name %{name}}

%global cpan_version_major 0.40
%global cpan_version_minor 05
%global cpan_version %{cpan_version_major}%{?cpan_version_minor}

Name:           %{?scl_prefix}perl-Module-Build
Epoch:          2
Version:        %{cpan_version_major}%{?cpan_version_minor:.%cpan_version_minor}
Release:        1%{?dist}
Summary:        Build and install Perl modules
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Build/
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/Module-Build-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl(Archive::Tar)
BuildRequires:  %{?scl_prefix}perl(AutoSplit)
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta) >= 2.110420
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta::YAML) >= 0.003
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Install) >= 0.3
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Installed)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Manifest) >= 1.54
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Mkbootstrap)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Packlist)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::ParseXS) >= 2.21
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Compare)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(File::ShareDir)
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.82
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(File::Temp) >= 0.15
BuildRequires:  %{?scl_prefix}perl(Getopt::Long)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(lib)
# perl(Module::Build) is loaded from ./lib
BuildRequires:  %{?scl_prefix}perl(Module::Metadata) >= 1.000002
BuildRequires:  %{?scl_prefix}perl(Parse::CPAN::Meta)
BuildRequires:  %{?scl_prefix}perl(Perl::OSType) >= 1
# Optional tests:
%if !%{defined perl_bootstrap} && ! 0%{?scl:1}
BuildRequires:  %{?scl_prefix}perl(Archive::Zip)
BuildRequires:  %{?scl_prefix}perl(PAR::Dist)
%if 0%{?fedora}  || 0%{?rhel} < 7
BuildRequires:  %{?scl_prefix}perl(Pod::Readme)
%endif
%endif
BuildRequires:  %{?scl_prefix}perl(Test::Harness) >= 3.16
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.49
BuildRequires:  %{?scl_prefix}perl(Text::ParseWords)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(version) >= 0.87
BuildRequires:  %{?scl_prefix}perl(warnings)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(CPAN::Meta) >= 2.110420
Requires:       %{?scl_prefix}perl(CPAN::Meta::YAML) >= 0.003
Requires:       %{?scl_prefix}perl(ExtUtils::CBuilder) >= 0.27
Requires:       %{?scl_prefix}perl(ExtUtils::Install) >= 0.3
Requires:       %{?scl_prefix}perl(ExtUtils::Manifest) >= 1.54
Requires:       %{?scl_prefix}perl(ExtUtils::Mkbootstrap)
Requires:       %{?scl_prefix}perl(ExtUtils::ParseXS) >= 2.21
Requires:       %{?scl_prefix}perl(Module::Metadata) >= 1.000002
# Keep PAR support optional (PAR::Dist)
Requires:       %{?scl_prefix}perl(Perl::OSType) >= 1
Requires:       %{?scl_prefix}perl(Test::Harness)
# Optional run-time needed for generating documentation from POD:
Requires:       %{?scl_prefix}perl(Pod::Html)
Requires:       %{?scl_prefix}perl(Pod::Man)
Requires:       %{?scl_prefix}perl(Pod::Text)

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((ExtUtils::Install|File::Spec|Module::Build|Module::Metadata|Perl::OSType)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(CPAN::Meta::YAML\\) >= 0.002$

%{?scl:
%filter_from_requires /perl(\(ExtUtils::Install|File::Spec|Module::Build|Module::Metadata|Perl::OSType\))\s*$/d
%filter_from_requires /perl(CPAN::Meta::YAML) >= 0.002$/d
%filter_setup
}

%description
Module::Build is a system for building, testing, and installing Perl
modules. It is meant to be an alternative to ExtUtils::MakeMaker.
Developers may alter the behavior of the module through sub-classing in a
much more straightforward way than with MakeMaker. It also does not require
a make on your system - most of the Module::Build code is pure-perl and
written in a very cross-platform way. In fact, you don't even need a shell,
so even platforms like MacOS (traditional) can use it fairly easily. Its
only prerequisites are modules that are included with perl 5.6.0, and it
works fine on perl 5.005 if you can install a few additional modules.

%prep
%setup -q -n Module-Build-%{cpan_version}

%build
%{?scl:scl enable %{scl} "}
perl Build.PL installdirs=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
./Build
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
./Build install destdir=%{buildroot} create_packlist=0
%{?scl:"}
%{_fixperms} %{buildroot}/*

%check
rm t/signature.t
%{?scl:scl enable %{scl} "}
LANG=C TEST_SIGNATURE=1 MB_TEST_EXPERIMENTAL=1 ./Build test
%{?scl:"}

%files
%doc Changes contrib LICENSE README
%{_bindir}/config_data
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.40.05-1
- 0.4005 bump

* Wed Feb 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.40.03-1
- SCL package - initial import
