%{?scl:%scl_package perl-Digest-SHA}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Digest-SHA
Epoch:          1
Version:        5.84
Release:        1%{?dist}
Summary:        Perl extension for SHA-1/224/256/384/512
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Digest-SHA/
Source0:        http://www.cpan.org/authors/id/M/MS/MSHELOR/Digest-SHA-%{version}.tar.gz
# Since 5.80, upstream overrides CFLAGS because they think it improves
# performance. Revert it.
Patch0:         Digest-SHA-5.84-Reset-CFLAGS.patch
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(Exporter)
# Optional run-time
BuildRequires:  %{?scl_prefix}perl(Digest::base)
# Optional tests
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.00
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage) >= 0.08
%endif
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(Carp)
# Optional but recommended
Requires:       %{?scl_prefix}perl(Digest::base)

%{?scl:
%filter_from_provides /\.so()/d
%filter_setup
}

%{?perl_default_filter}

%description
Digest::SHA is a complete implementation of the NIST Secure Hash Standard. It
gives Perl programmers a convenient way to calculate SHA-1, SHA-224, SHA-256,
SHA-384, SHA-512, SHA-512/224, and SHA-512/256 message digests. The module can
handle all types of input, including partial-byte data.

%prep
%setup -q -n Digest-SHA-%{version}
%patch0 -p1
chmod -x examples/*
%{?scl:scl enable %{scl} "}
perl -MExtUtils::MakeMaker -e 'ExtUtils::MM_Unix->fixin(q{examples/dups})'
%{?scl:"}

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
%doc Changes examples README
%{_bindir}/*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Digest*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.84-1
- 5.84 bump

* Fri Feb  8 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.82-1
- Stack package - initial release
