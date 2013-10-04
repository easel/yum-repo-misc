%{?scl:%scl_package perl-Text-Soundex}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Text-Soundex
Version:        3.04
Release:        1%{?dist}
Summary:        Implementation of the soundex algorithm
License:        Copyright only
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Text-Soundex/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Text-Soundex-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
# Carp not needed for tests
%if 0%(perl -e 'print $] > 5.017')
BuildRequires:  %{?scl_prefix}perl(deprecated)
%endif
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(if)
# Text::Unidecode not needed for tests
BuildRequires:  %{?scl_prefix}perl(XSLoader)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(Carp)
%if 0%(perl -e 'print $] > 5.017')
Requires:       %{?scl_prefix}perl(deprecated)
%endif
Requires:       %{?scl_prefix}perl(Text::Unidecode)

%{?perl_default_filter}

%description
Soundex is a phonetic algorithm for indexing names by sound, as pronounced in
English. This module implements the original soundex algorithm developed by
Robert Russell and Margaret Odell, as well as a variation called "American
Soundex".

%prep
%setup -q -n Text-Soundex-%{version}

%build
%{?scl:scl enable %{scl} '}
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{?scl:'}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Text*
%{_mandir}/man3/*

%changelog
* Thu Apr 04 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3.04-1
- SCL package - initial import
