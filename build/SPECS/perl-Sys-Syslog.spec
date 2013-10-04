%{?scl:%scl_package perl-Sys-Syslog}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Sys-Syslog
Version:        0.32
Release:        2%{?dist}
Summary:        Perl interface to the UNIX syslog(3) calls
# Unused sources fallback/* are covered with BSD license.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Sys-Syslog/
Source0:        http://www.cpan.org/authors/id/S/SA/SAPER/Sys-Syslog-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Constant)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Fcntl)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Socket)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
BuildRequires:  %{?scl_prefix}perl(warnings::register)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# DynaLoader not used
# Tests:
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Optional tests:
%if !%{defined perl_bootstrap}
%if !0%{?rhel}
BuildRequires:  %{?scl_prefix}perl(Test::Distribution)
%endif
BuildRequires:  %{?scl_prefix}perl(Test::NoWarnings)
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.14
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage) >= 1.06
%if ! 0%{?scl:1}
BuildRequires:  %{?scl_prefix}perl(Test::Portability::Files)
%endif
# POE::Component::Server::Syslog is not packaged yet
%endif
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(XSLoader)

%{?perl_default_filter}

%{?scl:
%filter_from_provides /\.so()/d
%filter_setup
}

%description
Sys::Syslog is an interface to the UNIX syslog(3) function. Call syslog() with
a string priority and a list of printf() arguments just like at syslog(3).

%prep
%setup -q -n Sys-Syslog-%{version}
chmod -x eg/*
# Inhibit bundled syslog.h
rm -rf fallback
sed -i -e '/^fallback\//d' MANIFEST
# Recode files
for F in Changes; do
    iconv -f ISO-8859-1 -t UTF-8 < "$F" >"${F}.utf8"
    touch -r "$F" "${F}.utf8"
    mv "${F}.utf8" "$F"
done

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
%doc Changes eg README 
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sys*
%{_mandir}/man3/*

%changelog
* Tue Jun 18 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-2
- Update a condition for BRs

* Tue Apr 30 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-1
- SCL package - initial import
