%{?scl:%scl_package perl-Data-Peek}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Data-Peek
Version:        0.38
Release:        1%{?dist}
Summary:        Collection of low-level debug facilities
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Peek/
Source0:        http://www.cpan.org/authors/id/H/HM/HMBRAND/Data-Peek-%{version}.tgz
# automatically create also DP.pm as alias of Data-Peek
Patch0:         Data-Peek-0.33.patch
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(Test::NoWarnings)
BuildRequires:  %{?scl_prefix}perl(warnings)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%{?perl_default_filter}

%{?scl:
%filter_from_provides /\.so()/d
%filter_setup
}

%description
Data::Peek started off as DDumper being a wrapper module over Data::Dumper,
but grew out to be a set of low-level data introspection utilities that no
other module provided yet, using the lowest level of the perl internals API
as possible.

%prep
%setup -q -n Data-Peek-%{version}
%patch0 -p1

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
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Data*
%{perl_vendorarch}/DP.pm
%{_mandir}/man3/*

%changelog
* Fri Apr 05 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-1
- SCL package - initial import
