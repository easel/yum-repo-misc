%{?scl:%scl_package perl-Clone}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Clone
Version:        0.34
Release:        1%{?dist}
Summary:        Recursively copy perl data types
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Clone
Source:         http://search.cpan.org/CPAN/authors/id/G/GA/GARU/Clone-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}perl(AutoLoader)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
BuildRequires:  %{?scl_prefix}perl(Taint::Runtime)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%{?perl_default_filter}

%{?scl:
%filter_from_provides /\.so()/d
%filter_setup
}

%description
This module provides a clone() method which makes recursive
copies of nested hash, array, scalar and reference types,
including tied variables and objects.

clone() takes a scalar argument and an optional parameter that
can be used to limit the depth of the copy. To duplicate lists,
arrays or hashes, pass them in by reference.

%prep
%setup -q -n Clone-%{version}
find . -type f -exec chmod -c -x {} ';'

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
chmod -R u+w %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes
%{perl_vendorarch}/auto/Clone/
%{perl_vendorarch}/Clone.pm
%{_mandir}/man3/*.3*

%changelog
* Mon Mar 11 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-1
- SCL package - initial import
