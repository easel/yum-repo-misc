%{?scl:%scl_package perl-IO-String}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-IO-String
Version:        1.08
Release:        1%{?dist}
Summary:        Emulate file interface for in-core strings
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/IO-String/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/IO-String-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Test)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(Data::Dumper)
Requires:       %{?scl_prefix}perl(IO::Handle)

%description
The "IO::String" module provides the "IO::File" interface for in-core
strings.  An "IO::String" object can be attached to a string, and
makes it possible to use the normal file operations for reading or
writing data, as well as for seeking to various locations of the
string.  This is useful when you want to use a library module that
only provides an interface to file handles on data that you have in a
string variable.

Note that perl-5.8 and better has built-in support for "in memory"
files, which are set up by passing a reference instead of a filename
to the open() call. The reason for using this module is that it makes
the code backwards compatible with older versions of Perl.


%prep
%setup -q -n IO-String-%{version}

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
chmod -R u+w %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes README
%{perl_vendorlib}/IO/
%{_mandir}/man3/*.3*


%changelog
* Mon Feb 11 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-1
- Stack package - initial release
