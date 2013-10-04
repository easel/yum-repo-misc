%{?scl:%scl_package perl-File-ShareDir}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-File-ShareDir
Version:        1.03
Release:        1%{?dist}
Summary:        Locate per-dist and per-module shared files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-ShareDir/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/File-ShareDir-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Class::Inspector) >= 1.12
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.47
Requires:       %{?scl_prefix}perl(Class::Inspector) >= 1.12
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude}|perl\\(Class::Inspector\\)$

%{?scl:
%filter_from_requires /perl(Class::Inspector)\s*$/d
%filter_setup
}

%description
The intent of File::ShareDir is to provide a companion to Class::Inspector
and File::HomeDir, modules that take a process that is well-known by
advanced Perl developers but gets a little tricky, and make it more
available to the larger Perl community.

%prep
%setup -q -n File-ShareDir-%{version}

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
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*
chmod 644 share/sample.txt
chmod 644 share/subdir/sample.txt
rm -rf %{buildroot}/blib/lib/auto/share/dist/File-ShareDir/
rm -rf %{buildroot}/blib/lib/auto/share/module/File-ShareDir/test_file.txt

%check
%{?scl:scl enable %{scl} "}
make test AUTOMATED_TESTING=1
%{?scl:"}

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Feb 15 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-1
- SCL package - initial import
