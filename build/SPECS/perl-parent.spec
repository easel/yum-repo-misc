%{?scl:%scl_package perl-parent}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}perl-parent
Epoch:		1
Version:	0.225
Release:	100%{?dist}
Summary:	Establish an ISA relationship with base classes at compile time
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/parent/
Source0:	http://search.cpan.org/CPAN/authors/id/C/CO/CORION/parent-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:	%{?scl_prefix}perl(lib)
BuildRequires:	%{?scl_prefix}perl(Test::More) >= 0.4
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:	%{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
Allows you to both load one or more modules, while setting up inheritance
from those modules at the same time. Mostly similar in effect to:

	package Baz;

	BEGIN {
		require Foo;
		require Bar;

		push @ISA, qw(Foo Bar);
	}

%prep
%setup -q -n parent-%{version}

# Remove spurious exec permissions
chmod -c -x Changes lib/parent.pm

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
rm -rf %{buildroot}
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} \; 2>/dev/null
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes 
%{perl_vendorlib}/parent.pm
%{_mandir}/man3/parent.3pm*

%changelog
* Wed Feb 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.225-100
- SCL package - initial import
