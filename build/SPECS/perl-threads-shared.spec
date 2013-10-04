%{?scl:%scl_package perl-threads-shared}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-threads-shared
Version:        1.43
Release:        1%{?dist}
Summary:        Perl extension for sharing data structures between threads
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/threads-shared/
Source0:        http://www.cpan.org/authors/id/J/JD/JDHEDDEN/threads-shared-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::testlib)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
BuildRequires:  %{?scl_prefix}perl(Test)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(threads) >= 1.73
BuildRequires:  %{?scl_prefix}perl(XSLoader)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(Carp)
Requires:       %{?scl_prefix}perl(threads) >= 1.73
Requires:       %{?scl_prefix}perl(XSLoader)

%{?perl_default_filter}

%{?scl:
%filter_from_provides /\.so()/d
%filter_setup
}

%description
By default, variables are private to each thread, and each newly created
thread gets a private copy of each existing variable. This module allows
you to share variables across different threads (and pseudo-forks on
Win32). It is used together with the threads module.

%prep
%setup -q -n threads-shared-%{version}

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
%{perl_vendorarch}/threads*
%{_mandir}/man3/*

%changelog
* Wed Feb 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.43-1
- SCL package - initial import
