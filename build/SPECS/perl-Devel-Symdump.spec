%{?scl:%scl_package perl-Devel-Symdump}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Devel-Symdump
Version:        2.10
Release:        1%{?dist}
Epoch:          1
Summary:        A Perl module for inspecting Perl's symbol table
Group:          Development/Libraries
License:        GPL+ or Artistic
Url:            http://search.cpan.org/dist/Devel-Symdump/
Source0:        http://www.cpan.org/authors/id/A/AN/ANDK/Devel-Symdump-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(English)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# File::Spec is optional and not really needed on Unices
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Test::Pod::Coverage -> Pod::Coverage -> Devel::Symdump
%if 0%{!?perl_bootstrap:1}
BuildRequires:  %{?scl_prefix}perl(Test::Pod)
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage)
%endif
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
The perl module Devel::Symdump provides a convenient way to inspect
perl's symbol table and the class hierarchy within a running program.

%prep
%setup -q -n Devel-Symdump-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} ';' 2>/dev/null
%{_fixperms} $RPM_BUILD_ROOT

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Changes README
%{perl_vendorlib}/Devel/
%{_mandir}/man3/Devel::Symdump.3pm*

%changelog
* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.10-1
- 2.10 bump

* Wed Feb 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.08-1
- SCL package - initial import
