%{?scl:%scl_package perl-Text-Glob}
%{!?scl:%global pkg_name %{name}}

Name: 		%{?scl_prefix}perl-Text-Glob
Version: 	0.09
Release: 	1%{?dist}
Summary: 	Perl module to match globbing patterns against text
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Text-Glob/
Source0: 	http://www.cpan.org/authors/id/R/RC/RCLAMP/Text-Glob-%{version}.tar.gz

BuildArch: noarch
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:  %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
Text::Glob implements glob(3) style matching that can be used to match
against text, rather than fetching names from a file-system.  If you
want to do full file globbing use the File::Glob module instead.

%prep
%setup -q -n Text-Glob-%{version}

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes
%{perl_vendorlib}/Text
%{_mandir}/man3/*

%changelog
* Thu Feb 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-1
- SCL package - initial import
