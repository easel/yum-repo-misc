%{?scl:%scl_package perl-IPC-Cmd}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-IPC-Cmd
# Epoch to compete with perl.spec
Epoch:          1
Version:        0.80
Release:        1%{?dist}
Summary:        Finding and running system commands made easy
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IPC-Cmd/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/IPC-Cmd-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(Locale::Maketext::Simple)
BuildRequires:  %{?scl_prefix}perl(Module::Load::Conditional)
BuildRequires:  %{?scl_prefix}perl(Params::Check) >= 0.20
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Socket)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Symbol)
BuildRequires:  %{?scl_prefix}perl(Text::ParseWords)
BuildRequires:  %{?scl_prefix}perl(vars)
# Tests:
# output.pl/IO::Handle not used
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# output.pl/warnings not used
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(Config)
Requires:       %{?scl_prefix}perl(ExtUtils::MakeMaker)
Requires:       %{?scl_prefix}perl(Params::Check) >= 0.20
Requires:       %{?scl_prefix}perl(POSIX)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Check\\)$

%{?scl:
%filter_from_requires /perl(Params::Check)\s*$/
%filter_setup
}

%description
IPC::Cmd allows you to run commands platform independently, interactively
if desired, but have them still work.

%prep
%setup -q -n IPC-Cmd-%{version}

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
* Thu Apr 04 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.80-1
- SCL package - initial import
