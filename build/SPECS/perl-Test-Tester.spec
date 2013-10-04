%{?scl:%scl_package perl-Test-Tester}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Test-Tester
Version:        0.108
Release:        1%{?dist}
Summary:        Ease testing test modules built with Test::Builder
License:        Artistic clarified
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Tester/
Source0:        http://www.cpan.org/authors/id/F/FD/FDALY/Test-Tester-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::Builder)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
If you have written a test module based on Test::Builder then Test::Tester
allows you to test it with the minimum of effort.

%prep
%setup -q -n Test-Tester-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
rm -rf $RPM_BUILD_ROOT

%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ARTISTIC CHANGES README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.108-1
- SCL package - initial import
