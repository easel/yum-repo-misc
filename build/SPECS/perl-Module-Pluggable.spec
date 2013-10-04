%{?scl:%scl_package perl-Module-Pluggable}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Module-Pluggable
# Epoch to compete with perl.spec
Epoch:          1
Version:        4.7
Release:        1%{?dist}
Summary:        Automatically give your module the ability to have plugins
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Pluggable/
Source0:        http://www.cpan.org/authors/id/S/SI/SIMONW/Module-Pluggable-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(FindBin)
BuildRequires:  %{?scl_prefix}perl(Module::Build)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions) >= 3.00
BuildRequires:  %{?scl_prefix}perl(if)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.62
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(File::Basename)
Requires:       %{?scl_prefix}perl(File::Spec::Functions) >= 3.00

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec::Functions\\)$

%{?scl:
%filter_from_requires /perl(File::Spec::Functions)\s*$/d
%filter_setup
}

%description
This package provides a simple but, hopefully, extensible way of having
'plugins' for your module. Essentially all it does is export a method into
your name space that looks through a search path for .pm files and turn those
into class names. Optionally it instantiates those classes for you.

%prep
%setup -q -n Module-Pluggable-%{version}
find -type f -exec chmod -x {} +

%build
%{?scl:scl enable %{scl} "}
perl Build.PL installdirs=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
./Build
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{?scl:"}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
./Build test
%{?scl:"}

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:4.7-1
- 4.7 bump

* Mon Feb 18 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:4.6-1
- SCL package - initial import

