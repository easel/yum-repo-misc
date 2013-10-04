%{?scl:%scl_package perl-DBD-SQLite}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-DBD-SQLite
Version:        1.29
Release:        1%{?dist}
Summary:        SQLite DBI Driver
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/DBD-SQLite/
Source0:        http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/DBD-SQLite-%{version}.tar.gz
Patch0:         perl-DBD-SQLite-bz543982.patch
# if sqlite >= 3.1.3 then
#   perl-DBD-SQLite uses the external library
# else
#   perl-DBD-SQLite is self-contained (uses the sqlite local copy)
BuildRequires:  sqlite-devel
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Prevent bug #443495
BuildRequires:  %{?scl_prefix}perl(DBI) >= 1.607
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests only
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Encode)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Fatal)
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.82
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(locale)
BuildRequires:  %{?scl_prefix}perl(Test::Builder)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.42
BuildRequires:  %{?scl_prefix}perl(utf8)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%{?perl_default_filter}

%{?scl:
%filter_from_provides /\.so()/d
%filter_setup
}

%description
SQLite is a public domain RDBMS database engine that you can find at
http://www.hwaci.com/sw/sqlite/.

This module provides a SQLite RDBMS module that uses the system SQLite 
libraries.

%prep
%setup -q -n DBD-SQLite-%{version}
%patch0 -p1 -b .bz543982

%build
%{?scl:scl enable %{scl} '}
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
%{?scl:'}
%{?scl:scl enable %{scl} '}
make %{?_smp_mflags} OPTIMIZE="%{optflags}"
%{?scl:'}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f \( -name .packlist -o \
     -name '*.bs' -size 0 \) -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/DBD/
%{_mandir}/man3/*.3pm*

%changelog
* Thu Jul 04 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.29-1
- SCL package - initial import
