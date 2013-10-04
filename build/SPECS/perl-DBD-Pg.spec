%{?scl:%scl_package perl-DBD-Pg}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-DBD-Pg
Summary:        A PostgreSQL interface for perl
Version:        2.19.3
Release:        1%{?dist}
License:        GPLv2+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/T/TU/TURNSTEP/DBD-Pg-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/DBD-Pg/
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

# Prevent bug #443495
BuildRequires:  %{?scl_prefix}perl(DBI) >= 1.607
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.61
BuildRequires:  %{?scl_prefix}perl(version)
BuildRequires:  postgresql-devel >= 7.4
BuildRequires:  %{?scl_prefix}perl(Test::Simple), postgresql-server

Requires:       %{?scl_prefix}perl(DBI) >= 1.52
# test requirements
Requires:       %{?scl_prefix}perl(Data::Peek)
# Missed by the find provides script:
Provides:       %{?scl_prefix}perl(DBD::Pg) = %{version}

%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DBD::Pg\\)$
%{?perl_default_subpackage_tests}

%{?scl:
%filter_from_provides /\.so()/d
%filter_from_provides /perl(DBD::Pg)\s*$/d
%filter_setup
}

%description
DBD::Pg is a Perl module that works with the DBI module to provide access
to PostgreSQL databases.

%prep
%setup -q -n DBD-Pg-%{version}

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
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
# Full test coverage requires a live PostgreSQL database (see the README file)
#export DBI_DSN=dbi:Pg:dbname=<database>
#export DBI_USER=<username>
#export DBI_PASS=<password>
# If variables undefined, package test will create it's own database.
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes README README.dev TODO
%{perl_vendorarch}/DBD/
%{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/Bundle/DBD/Pg.pm
%{_mandir}/man3/*.3*

%changelog
* Mon Apr 08 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.19.3-1
- SCL package - initial import
