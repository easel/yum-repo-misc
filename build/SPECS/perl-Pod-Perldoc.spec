%{?scl:%scl_package perl-Pod-Perldoc}
%{!?scl:%global pkg_name %{name}}

%global cpan_version 3.20
Name:           %{?scl_prefix}perl-Pod-Perldoc
# let's overwrite the module from perl.srpm
Version:        %(echo '%{cpan_version}' | sed 's/_/./')
Release:        1%{?dist}
Summary:        Look up Perl documentation in Pod format
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Pod-Perldoc/
Source0:        http://www.cpan.org/authors/id/M/MA/MALLEN/Pod-Perldoc-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Run-time:
# Pod::Perldoc::ToMan executes roff
BuildRequires:  groff
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Encode)
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(File::Temp) >= 0.22
BuildRequires:  %{?scl_prefix}perl(HTTP::Tiny)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(IO::Select)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(parent)
BuildRequires:  %{?scl_prefix}perl(Pod::Man) >= 2.18
BuildRequires:  %{?scl_prefix}perl(Pod::Simple::Checker)
BuildRequires:  %{?scl_prefix}perl(Pod::Simple::RTF) >= 3.16
BuildRequires:  %{?scl_prefix}perl(Pod::Simple::XMLOutStream) >= 3.16
BuildRequires:  %{?scl_prefix}perl(Pod::Text)
BuildRequires:  %{?scl_prefix}perl(Pod::Text::Color)
BuildRequires:  %{?scl_prefix}perl(Pod::Text::Termcap)
BuildRequires:  %{?scl_prefix}perl(Symbol)
BuildRequires:  %{?scl_prefix}perl(Text::ParseWords)
# Tests:
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Optional tests:
%if !%{defined perl_bootstrap}
%if !( 0%{?rhel} >= 7 ) && ! 0%{?scl:1}
BuildRequires:  %{?scl_prefix}perl(Tk)
BuildRequires:  %{?scl_prefix}perl(Tk::Pod)
%endif
%endif
# Pod::Perldoc::ToMan executes roff
Requires:       groff
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(Encode)
Requires:       %{?scl_prefix}perl(File::Temp) >= 0.22
Requires:       %{?scl_prefix}perl(HTTP::Tiny)
Requires:       %{?scl_prefix}perl(IO::Handle)
Requires:       %{?scl_prefix}perl(lib)
Requires:       %{?scl_prefix}perl(Pod::Man) >= 2.18
Requires:       %{?scl_prefix}perl(Pod::Simple::Checker)
Requires:       %{?scl_prefix}perl(Pod::Simple::RTF) >= 3.16
Requires:       %{?scl_prefix}perl(Pod::Simple::XMLOutStream) >= 3.16
Requires:       %{?scl_prefix}perl(Text::ParseWords)
# Tk is optional
Requires:       %{?scl_prefix}perl(Symbol)

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Pod::Man|Pod::Simple::XMLOutStream|Pod::Simple::RTF\\)\\s*$

%{?scl:
%filter_from_requires /perl(\(Pod::Man|Pod::Simple::XMLOutStream|Pod::Simple::RTF\))\s*$/d
%filter_setup
}

%description
perldoc looks up a piece of documentation in .pod format that is embedded
in the perl installation tree or in a perl script, and displays it via
"groff -man | $PAGER". This is primarily used for the documentation for
the perl library modules.

%prep
%setup -q -n Pod-Perldoc-%{cpan_version}

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
%{_bindir}/perldoc
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue May 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3.20-1
- 3.20 bump

* Wed Feb 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3.19.01-1
- SCL package - initial import
