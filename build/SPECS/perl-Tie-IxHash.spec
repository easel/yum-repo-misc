%{?scl:%scl_package perl-Tie-IxHash}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Tie-IxHash
Version:        1.22
Release:        10%{?dist}
Summary:        Ordered associative arrays for Perl

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Tie-IxHash/
Source0:        http://search.cpan.org/CPAN/authors/id/C/CH/CHORNY/Tie-IxHash-%{version}.tar.gz
Patch0:         Tie-IxHash-1.22-Makefile.patch
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker), %{?scl_prefix}perl(Test::More)
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(Test::Pod)
%endif
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
This Perl module implements Perl hashes that preserve the order in
which the hash elements were added. The order is not affected when
values corresponding to existing keys in the IxHash are changed.
The elements can also be set to any arbitrary supplied order. The
familiar perl array operations can also be performed on the IxHash.


%prep
%setup -q -n Tie-IxHash-%{version}

# Fix Makefile.PL to work with old ExtUtils::MakeMaker versions
%patch0 -p1

# Fix line endings
sed -i -e 's/\r$//' Changes README


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
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} ';' 2>/dev/null
chmod -R u+w $RPM_BUILD_ROOT/*


%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/Tie/
%{_mandir}/man3/*.3pm*


%changelog
* Thu Feb 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-1
- SCL package - initial import
