%{?scl:%scl_package perl-B-Lint}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-B-Lint
Version:        1.17
Release:        1%{?dist}
Summary:        Perl lint
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/B-Lint/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/B-Lint-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Run-Time
BuildRequires:  %{?scl_prefix}perl(B) 
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
%if 0%(perl -e 'print $] > 5.017')
BuildRequires:  %{?scl_prefix}perl(deprecated)
%endif
BuildRequires:  %{?scl_prefix}perl(if)
BuildRequires:  %{?scl_prefix}perl(List::Util)
BuildRequires:  %{?scl_prefix}perl(Module::Pluggable)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(strict)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(O)
BuildRequires:  %{?scl_prefix}perl(warnings)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(constant)
%if 0%(perl -e 'print $] > 5.017')
Requires:       %{?scl_prefix}perl(deprecated)
%endif

%description
The B::Lint module is equivalent to an extended version of the -w option of
perl. It is named after the program lint which carries out a similar process
for C programs.

%prep
%setup -q -n B-Lint-%{version}
# Install into architercture-agnostic path, CPAN RT #83049
sed -i '/PM *=>/,/}/d' Makefile.PL

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Apr 04 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-1
- SCL package - initial import
