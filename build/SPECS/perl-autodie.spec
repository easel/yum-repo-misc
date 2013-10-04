%{?scl:%scl_package perl-autodie}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-autodie
Version:        2.16
Release:        1%{?dist}
Summary:        Replace functions with ones that succeed or die
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/autodie/
Source0:        http://www.cpan.org/authors/id/P/PJ/PJF/autodie-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
# Stick on bundled inc::Module::Install to allow boot-straping this core package
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MM_Unix)
BuildRequires:  %{?scl_prefix}perl(FindBin)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(B)
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Fcntl)
BuildRequires:  %{?scl_prefix}perl(if)
# Keep IPC::System::Simple 0.12 optional
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Tie::RefHash)
# Sub::Identify is optional
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests:
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(open)
BuildRequires:  %{?scl_prefix}perl(Socket)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(B)
Requires:       %{?scl_prefix}perl(Fcntl)
Requires:       %{?scl_prefix}perl(overload)
Requires:       %{?scl_prefix}perl(POSIX)

%description
The "autodie" and "Fatal" pragma provides a convenient way to replace
functions that normally return false on failure with equivalents that throw an
exception on failure.

However "Fatal" has been obsoleted by the new autodie pragma. Please use
autodie in preference to "Fatal".

%prep
%setup -q -n autodie-%{version}
find -type f -exec chmod -x {} +

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
%doc AUTHORS Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Apr 03 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.16-1
- SCL package - initial import
