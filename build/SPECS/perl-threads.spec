%{?scl:%scl_package perl-threads}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-threads
Version:        1.86
Release:        100%{?dist}
Summary:        Perl interpreter-based threads
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/threads/
Source0:        http://search.cpan.org/CPAN/authors/id/J/JD/JDHEDDEN/threads-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::testlib)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# Tests only:
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(Carp)

%{?perl_default_filter}

%{?scl:
%filter_from_provides /\.so()/d
%filter_setup
}

%description
Since Perl 5.8, thread programming has been available using a model called
interpreter threads which provides a new Perl interpreter for each thread,
and, by default, results in no data or state information being shared
between threads.

(Prior to Perl 5.8, 5005threads was available through the "Thread.pm" API.
This threading model has been deprecated, and was removed as of Perl 5.10.0.)

%prep
%setup -q -n threads-%{version}

%build
%{?scl:scl enable %{scl} '}
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
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
%{perl_vendorarch}/threads*
%{_mandir}/man3/*

%changelog
* Wed Feb 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.86-100
- SCL package - initial import
