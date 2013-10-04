%{?scl:%scl_package perl-Number-Compare}
%{!?scl:%global pkg_name %{name}}

Name: 		%{?scl_prefix}perl-Number-Compare
Version: 	0.03
Release: 	1%{?dist}
Summary: 	Perl module for numeric comparisons
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Number-Compare/
Source0: 	http://www.cpan.org/authors/id/R/RC/RCLAMP/Number-Compare-%{version}.tar.gz

BuildArch: 	noarch
BuildRequires:	%{?scl_prefix}perl(Carp)
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:	%{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:  	%{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
Number::Compare compiles a simple comparison to an anonymous subroutine,
which you can call with a value to be tested again.

%prep
%setup -q -n Number-Compare-%{version}

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
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/Number
%{_mandir}/man3/*

%changelog
* Thu Feb 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-1
- SCL package - initial import
