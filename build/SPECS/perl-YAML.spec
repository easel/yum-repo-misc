%{?scl:%scl_package perl-YAML}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-YAML
Version:        0.84
Release:        1%{?dist}
Summary:        YAML Ain't Markup Language (tm)
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/YAML/
Source0:        http://search.cpan.org/CPAN/authors/id/M/MS/MSTROUT/YAML-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(lib)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(Carp)
Requires:       %{?scl_prefix}perl(Data::Dumper)

# Filter private provides:
# perl(yaml_mapping) perl(yaml_scalar) perl(yaml_sequence)
%global __provides_exclude ^perl\\(yaml_
%{?scl:
%filter_from_provides /perl(yaml_/d
%filter_setup
}

%description
The YAML.pm module implements a YAML Loader and Dumper based on the
YAML 1.0 specification. http://www.yaml.org/spec/
YAML is a generic data serialization language that is optimized for
human readability. It can be used to express the data structures of
most modern programming languages, including Perl.
For information on the YAML syntax, please refer to the YAML
specification.

%prep
%setup -q -n YAML-%{version}

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

# Removing Test::YAML (at least temporarily) due
# to security concerns and questionable value.
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=197539
rm -f %{buildroot}%{perl_vendorlib}/Test/YAML* \
    %{buildroot}%{_mandir}/man3/Test::YAML*.3*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes README LICENSE
%{perl_vendorlib}/YAML*
%{_mandir}/man3/YAML*.3*

%changelog
* Wed Feb  6 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-1
- Stack package - initial release
