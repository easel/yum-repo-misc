%{?scl:%scl_package perl-Class-Inspector}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}perl-Class-Inspector
Version:	1.28
Release:	2%{?dist}
Summary:	Get information about a class and its structure
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Class-Inspector/
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Class-Inspector-%{version}.tar.gz

%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:  %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
BuildArch: noarch

BuildRequires:	%{?scl_prefix}perl(Exporter)
BuildRequires:	%{?scl_prefix}perl(Test::More)
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:	%{?scl_prefix}perl(File::Spec) >= 0.80

%if !%{defined perl_bootstrap} && ! 0%{?scl:1}
BuildRequires: %{?scl_prefix}perl(Test::Pod) >= 1.44
BuildRequires: %{?scl_prefix}perl(Test::CPAN::Meta) >= 0.17
BuildRequires: %{?scl_prefix}perl(Perl::MinimumVersion) >= 1.27
BuildRequires: %{?scl_prefix}perl(Test::MinimumVersion) >= 0.101080
%endif

%description
Class::Inspector allows you to get information about a loaded class.
Most or all of this information can be found in other ways, but they aren't
always very friendly, and usually involve a relatively high level of Perl
wizardry, or strange and unusual looking code. Class::Inspector attempts to
provide an easier, more friendly interface to this information.

%prep
%setup -q -n Class-Inspector-%{version}

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
%if !%{defined perl_bootstrap} && ! 0%{?scl:1}
%{?scl:scl enable %{scl} "}
make test AUTOMATED_TESTING=1
%{?scl:"}
%else
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}
%endif

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/Class
%{_mandir}/man3/*

%changelog
* Tue Apr 09 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.28-2
- Update condition for BRs

* Fri Feb 15 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.28-1
- SCL package - initial import
