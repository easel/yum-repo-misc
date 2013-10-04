%{?scl:%scl_package perl-Net-Daemon}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Net-Daemon
Version:        0.48
Release:        1%{?dist}
Summary:        Perl extension for portable daemons

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Net-Daemon/
Source0:        http://search.cpan.org/CPAN/authors/id/M/MN/MNOONING/Net-Daemon-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl-Pod-Perldoc
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Getopt::Long)
# Tests:
BuildRequires:  %{?scl_prefix}perl(IO::Socket)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Network tests:
%{?_with_network_tests:
BuildRequires:  %{?scl_prefix}perl(lib)
}
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
Net::Daemon is an abstract base class for implementing portable server 
applications in a very simple way. The module is designed for Perl 5.006 and 
ithreads (and higher), but can work with fork() and Perl 5.004.

The Net::Daemon class offers methods for the most common tasks a daemon 
needs: Starting up, logging, accepting clients, authorization, restricting 
its own environment for security and doing the true work. You only have to 
override those methods that aren't appropriate for you, but typically 
inheriting will safe you a lot of work anyways.


%prep
%setup -q -n Net-Daemon-%{version}
# Convert EOL
sed -i 's/\r//' README

# generate our other two licenses...
perldoc perlgpl > LICENSE.GPL
perldoc perlartistic > LICENSE.Artistic


%build
%{?scl:scl enable %{scl} '}
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{?scl:'}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}


%install
rm -rf $RPM_BUILD_ROOT
%{?scl:scl enable %{scl} "}
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
# Remove the next line from noarch packages (unneeded)
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
%{?!_with_network_tests:
# Disable tests which will fail under mock
  rm t/config*
  rm t/fork*
  rm t/ithread*
  rm t/loop*
  rm t/single.t
  rm t/unix.t
}

%{?scl:scl enable %{scl} "}
make test
%{?scl:"}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog README LICENSE.*
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Mon Mar 11 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-1
- SCL package - initial import
