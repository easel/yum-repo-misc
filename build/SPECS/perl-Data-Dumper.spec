%{?scl:%scl_package perl-Data-Dumper}
%{!?scl:%global pkg_name %{name}}

%global cpan_version 2.145
Name:           %{?scl_prefix}perl-Data-Dumper
Version:        %(echo '%{cpan_version}' | tr '_' '.')
Release:        2%{?dist}
Summary:        Stringify perl data structures, suitable for printing and eval
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Dumper/
Source0:        http://www.cpan.org/authors/id/S/SM/SMUELLER/Data-Dumper-%{cpan_version}.tar.gz
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(B::Deparse)
BuildRequires:  %{?scl_prefix}perl(bytes)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# perl-Test-Simple is in cycle with perl-Data-Dumper
%if !%{defined perl_bootstrap}
# Tests only:
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.98
# Optional tests:
BuildRequires:  %{?scl_prefix}perl(Encode)
%endif
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(B::Deparse)
Requires:       %{?scl_prefix}perl(bytes)
Requires:       %{?scl_prefix}perl(Scalar::Util)
Requires:       %{?scl_prefix}perl(XSLoader)

%{?scl:%filter_from_provides /\.so()/d}
%{?scl:%filter_setup}

%{?perl_default_filter}

%description
Given a list of scalars or reference variables, writes out their contents
in perl syntax. The references can also be objects. The content of each
variable is output in a single Perl statement. Handles self-referential
structures correctly.

%prep
%setup -q -n Data-Dumper-%{cpan_version}
sed -i '/MAN3PODS/d' Makefile.PL

%build
%{?scl:scl enable %{scl} '}
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{?scl:'}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if !%{defined perl_bootstrap}
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}
%endif

%files
%doc Changes Todo
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Data*
%{_mandir}/man3/*

%changelog
* Tue Jun 18 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.145-2
- Rebuild with disabled perl_bootstrap macro

* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.145-1
- 2.145 bump

* Fri Feb  8 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.139-1
- Stack package - initial release
