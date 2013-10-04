%{?scl:%scl_package perl-File-Copy-Recursive}
%{!?scl:%global pkg_name %{name}}

Name: 		%{?scl_prefix}perl-File-Copy-Recursive
Version: 	0.38
Release: 	1%{?dist}
Summary: 	Extension for recursively copying files and directories 
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/File-Copy-Recursive/
Source0: 	http://www.cpan.org/modules/by-module/File/File-Copy-Recursive-%{version}.tar.gz
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:  %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
BuildArch: noarch
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:	%{?scl_prefix}perl(File::Spec)
BuildRequires:	%{?scl_prefix}perl(Test::More)

%description
This module copies and moves directories recursively to an optional depth and
attempts to preserve each file or directory's mode.

%prep
%setup -q -n File-Copy-Recursive-%{version}

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes README
%{perl_vendorlib}/File
%{_mandir}/man3/*

%changelog
* Tue Feb 12 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-1
- SCL package - initial release
