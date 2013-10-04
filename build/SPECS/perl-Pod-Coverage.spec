%{?scl:%scl_package perl-Pod-Coverage}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Pod-Coverage
Version:        0.23
Release:        2%{?dist}
Summary:        Checks if the documentation of a module is comprehensive
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Pod-Coverage/
Source0:        http://www.cpan.org/authors/id/R/RC/RCLAMP/Pod-Coverage-%{version}.tar.gz
# Make pod_cover more secure, CPAN RT#85540
Patch0:         Pod-Coverage-0.23-Do-not-search-.-lib-by-pod_cover.patch
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(B)
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(Devel::Symdump) >= 2.01
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Pod::Find) >= 0.21
BuildRequires:  %{?scl_prefix}perl(Pod::Parser) >= 1.13
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(Test::Pod)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
Requires:       %{?scl_prefix}perl(Devel::Symdump) >= 2.01
Requires:       %{?scl_prefix}perl(Pod::Find) >= 0.21
Requires:       %{?scl_prefix}perl(Pod::Parser) >= 1.13
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Devel::Symdump\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Pod::Find\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Pod::Parser\\)$

%{?scl:
%filter_from_requires /perl(Devel::Symdump)\s*$/d
%filter_from_requires /perl(Pod::Find)\s*$/d
%filter_from_requires /perl(Pod::Parser)\s*$/d
%filter_setup
}

%description
Developers hate writing documentation.  They'd hate it even more if their
computer tattled on them, but maybe they'll be even more thankful in the
long run.  Even if not, perlmodstyle tells you to, so you must obey.

This module provides a mechanism for determining if the pod for a given
module is comprehensive.

%prep
%setup -q -n Pod-Coverage-%{version}
%patch0 -p1

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
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes examples
%{_bindir}/pod_cover
%{perl_vendorlib}/Pod/
%{_mandir}/man3/Pod::Coverage.3pm*
%{_mandir}/man3/Pod::Coverage::CountParents.3pm*
%{_mandir}/man3/Pod::Coverage::ExportOnly.3pm*
%{_mandir}/man3/Pod::Coverage::Overloader.3pm*

%changelog
* Thu May 23 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-2
- Do not put ./lib into @INC by pod_cover tool (ppisar)

* Tue May 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-1
- 0.23 bump

* Wed Feb 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-1
- SCL package - initial import
