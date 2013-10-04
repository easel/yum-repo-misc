%{?scl:%scl_package perl-CGI}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-CGI
Summary:        Handle Common Gateway Interface requests and responses
Version:        3.63
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/M/MA/MARKSTOS/CGI.pm-%{version}.tar.gz
URL:            http://search.cpan.org/dist/CGI
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Run-requires:
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(FCGI) >= 0.67
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.82
# Apache modules are optional
# Tests:
BuildRequires:  %{?scl_prefix}perl(Encode)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.98
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(FCGI) >= 0.67
Requires:       %{?scl_prefix}perl(File::Spec) >= 0.82
Obsoletes:      %{?scl_prefix}%{pkg_name}-tests <= 3.49

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((FCGI|File::Spec)\\)$
# Remove false provides
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\((Fh|MultipartBuffer)\\)$

%{?scl:
%filter_from_provides /perl(\(MultipartBuffer\|Fh\))\s*$/d
%filter_from_requires /perl(\(FCGI\|File::Spec\))\s*$/d
%filter_setup
}

%description
CGI.pm is a stable, complete and mature solution for processing and preparing
HTTP requests and responses. Major features including processing form
submissions, file uploads, reading and writing cookies, query string
generation and manipulation, and processing and preparing HTTP headers. Some
HTML generation utilities are included as well.

CGI.pm performs very well in in a vanilla CGI.pm environment and also comes 
with built-in support for mod_perl and mod_perl2 as well as FastCGI.

%prep
%setup -q -n CGI.pm-%{version}
iconv -f iso8859-1 -t utf-8 < Changes > Changes.1
mv Changes.1 Changes
sed -i 's?usr/bin perl?usr/bin/perl?' t/init.t

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc cgi_docs.html Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Wed Feb  6 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3.63-1
- Stack package - initial release

