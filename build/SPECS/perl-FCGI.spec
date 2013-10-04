%{?scl:%scl_package perl-FCGI}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-FCGI
Summary:        FastCGI Perl bindings
# needed to properly replace/obsolete fcgi-perl
Epoch:          1
Version:        0.74
Release:        1%{?dist}
# same as fcgi
License:        OML
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/FCGI-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/FCGI
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Liblist)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(Getopt::Long)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(Test)
Provides:       %{?scl_prefix}fcgi-perl =  %{epoch}:%{version}-%{release}
Obsoletes:      %{?scl_prefix}fcgi-perl =< 2.4.0
# Dropped during f19 development cycle
#Obsoletes:      %%{?scl_prefix}%%{pkg_name}-tests <= 0.74-6

%{?perl_default_filter}

%{?scl:
%filter_from_provides /\.so()/d
%filter_setup
}

%description
%{summary}.

%prep
%setup -q -n FCGI-%{version}
find . -type f -exec chmod -c -x {} +

%build
%{?scl:scl enable %{scl} '}
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{?scl:'}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc ChangeLog README LICENSE.TERMS echo.PL remote.PL threaded.PL
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_mandir}/man3/*.3*

%changelog
* Mon Feb  4 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.74-1
- Stack package - initial release
