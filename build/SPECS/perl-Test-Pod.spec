%{?scl:%scl_package perl-Test-Pod}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Test-Pod
Version:        1.48
Release:        1%{?dist}
Summary:        Test POD files for correctness
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-Pod/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DW/DWHEELER/Test-Pod-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(Module::Build) >= 0.30
BuildRequires:  %{?scl_prefix}perl(Pod::Simple) >= 3.05
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Test::Builder)
BuildRequires:  %{?scl_prefix}perl(Test::Builder::Tester) >= 1.02
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.62
BuildRequires:  %{?scl_prefix}perl(warnings)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(Pod::Simple) >= 3.05
Requires:       %{?scl_prefix}perl(Test::Builder::Tester) >= 1.02
Requires:       %{?scl_prefix}perl(Test::More) >= 0.62

%description
Check POD files for errors or warnings in a test file, using Pod::Simple to do
the heavy lifting.

%prep
%setup -q -n Test-Pod-%{version}

%build
%{?scl:scl enable %{scl} "}
perl Build.PL installdirs=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
./Build
%{?scl:"}


%install
%{?scl:scl enable %{scl} "}
./Build install destdir=%{buildroot} create_packlist=0
%{?scl:"}
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} \; 2>/dev/null
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} - << \EOF}
LC_ALL=C ./Build test
%{?scl:EOF}

%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Pod.3pm*

%changelog
* Tue May 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.48-1
- 1.48 bump

* Wed Feb 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.46-1
- SCL package - initial import
