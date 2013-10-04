%{?scl:%scl_package perl-DBIx-Simple}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-DBIx-Simple
Summary:        Easy-to-use OO interface to DBI
Version:        1.35
Release:        1%{?dist}
License:        Public Domain
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/J/JU/JUERD/DBIx-Simple-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/DBIx-Simple/
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}perl(DBI) >= 1.21
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(Test::More)
Requires:       %{?scl_prefix}perl(DBI) >= 1.21


%{?perl_default_filter}

%{?scl:
%filter_from_provides /\.so()/d
%filter_setup
}

%description
DBIx::Simple provides a simplified interface to DBI, Perl's powerful
database module.

%prep
%setup -q -n DBIx-Simple-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{?scl:"}

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Apr 08 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.35-1
- SCL package - initial import
