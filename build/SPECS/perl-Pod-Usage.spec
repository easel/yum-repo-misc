%{?scl:%scl_package perl-Pod-Usage}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Pod-Usage
Version:        1.61
Release:        1%{?dist}
Summary:        Print a usage message from embedded pod documentation
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Pod-Usage/
Source0:        http://www.cpan.org/authors/id/M/MA/MAREKR/Pod-Usage-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Pod::Select)
# Pod::Usage executes perldoc from perl-Pod-Perldoc by default
BuildRequires:  %{?scl_prefix}perl-Pod-Perldoc
BuildRequires:  %{?scl_prefix}perl(Pod::Text)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(FileHandle)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.6
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
# Pod::Usage executes perldoc from perl-Pod-Perldoc by default
Requires:       %{?scl_prefix}perl-Pod-Perldoc
Requires:       %{?scl_prefix}perl(Pod::Text)

%description
pod2usage will print a usage message for the invoking script (using its
embedded POD documentation) and then exit the script with the desired exit
status. The usage message printed may have any one of three levels of
"verboseness": If the verbose level is 0, then only a synopsis is printed.
If the verbose level is 1, then the synopsis is printed along with a
description (if present) of the command line options and arguments. If the
verbose level is 2, then the entire manual page is printed.

%prep
%setup -q -n Pod-Usage-%{version}
find -type f -exec chmod a-x {} +
for F in CHANGES README; do
    sed -i -e 's/\r//' "$F"
done

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
%doc CHANGES README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Feb 18 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.61-1
- SCL package - initial import
