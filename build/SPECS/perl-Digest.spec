%{?scl:%scl_package perl-Digest}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Digest
Version:        1.17
Release:        100%{?dist}
Summary:        Modules that calculate message digests
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Digest/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/Digest-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(MIME::Base64)
# Tests only:
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.47
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(MIME::Base64)

%description
The Digest:: modules calculate digests, also called "fingerprints" or
"hashes", of some data, called a message. The digest is (usually)
some small/fixed size string. The actual size of the digest depend of
the algorithm used. The message is simply a sequence of arbitrary
bytes or bits.

%prep
%setup -q -n Digest-%{version}
chmod -x digest-bench

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

%files
%doc Changes digest-bench README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue May 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-100
- Increase release number to supersede perl sub-package

* Fri Feb  8 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-1
- Stack package - initial release
