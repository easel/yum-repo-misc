%{?scl:%scl_package perl-Taint-Runtime}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Taint-Runtime
Version:        0.03
Release:        1%{?dist}
Summary:        Runtime enable taint checking
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Taint-Runtime
Source0:        http://search.cpan.org/CPAN/authors/id/R/RH/RHANDOM/Taint-Runtime-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# Tests:
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
This module enables run-time taint checking, for cases where the -T
switch on the command line is not appropriate or viable. There are
a somewhat limited number of legitimate use cases where you should 
use this module instead of the -T switch. Unless you have a specific and
good reason for not using the -T option, you should use the -T option.

%prep
%setup -q -n Taint-Runtime-%{version}
chmod +x is_taint_bench.pl

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
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes README
%{perl_vendorarch}/auto/Taint/
%{perl_vendorarch}/Taint/
%{_mandir}/man3/*.3*

%changelog
* Mon Mar 11 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-1
- SCL package - initial im port
