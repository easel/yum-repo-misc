%{?scl:%scl_package perl-File-CheckTree}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-File-CheckTree
Version:        4.42
Release:        1%{?dist}
Summary:        Run many file-test checks on a tree
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-CheckTree/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/File-CheckTree-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Cwd)
%if 0%(perl -e 'print $] > 5.017')
BuildRequires:  %{?scl_prefix}perl(deprecated)
%endif
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(if)
# Tests:
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
%if 0%(perl -e 'print $] > 5.017')
Requires:       %{?scl_prefix}perl(deprecated)
%endif

%description
File::CheckTree::validate() routine takes a single multi-line string
consisting of directives, each containing a file name plus a file test to try
on it. (The file test may also be a "cd", causing subsequent relative file
names to be interpreted relative to that directory.) After the file test you
may put || die to make it a fatal error if the file test fails. The default is
|| warn.  The file test may optionally have a "!' prepended to test for the
opposite condition. If you do a cd and then list some relative file names, you
may want to indent them slightly for readability. If you supply your own die()
or warn() message, you can use $file to interpolate the file name.

%prep
%setup -q -n File-CheckTree-%{version}

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
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Apr 04 2013 Jitka Plesnikova <jplesnik@redhat.com> - 4.42-1
- SCL package - initial import
