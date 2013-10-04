%{?scl:%scl_package perl-PlRPC}
%{!?scl:%global pkg_name %{name}}

Name:       %{?scl_prefix}perl-PlRPC 
Version:    0.2020 
Release:    1%{?dist}
License:    GPL+ or Artistic
Group:      Development/Libraries
Summary:    Interface for writing PlRPC clients and servers
Url:        http://search.cpan.org/dist/PlRPC
Source:     http://search.cpan.org/CPAN/authors/id/M/MN/MNOONING/PlRPC/PlRPC-%{version}.tar.gz 
# See <https://rt.cpan.org/Public/Bug/Display.html?id=74430>
Patch0:     %{pkg_name}-0.2020-Do-not-use-syslog.patch
BuildArch:  noarch
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# perldoc utility is called from Makefile
BuildRequires:  %{?scl_prefix}perl-Pod-Perldoc
# Run-time
BuildRequires:  %{?scl_prefix}perl(Compress::Zlib)
BuildRequires:  %{?scl_prefix}perl(IO::Socket)
BuildRequires:  %{?scl_prefix}perl(Net::Daemon) >= 0.13
BuildRequires:  %{?scl_prefix}perl(Net::Daemon::Log)
BuildRequires:  %{?scl_prefix}perl(Net::Daemon::Test)
BuildRequires:  %{?scl_prefix}perl(Storable)
# Optionable tests
%if ! 0%{?scl:1}
BuildRequires:  %{?scl_prefix}perl(Crypt::DES)
%endif
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
# Compress::Zlib is needed for optional compression
Requires:       %{?scl_prefix}perl(Compress::Zlib)
Requires:       %{?scl_prefix}perl(Net::Daemon) >= 0.13

# Remove undespecified dependencies
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(Net::Daemon\\)$

%{?scl:
%filter_from_requires /perl(Net::Daemon)\s*$/
%filter_setup
}


%description
PlRPC (Perl RPC) is a package that simplifies the writing of Perl based
client/server applications. RPC::PlServer is the package used on the
server side, and you guess what RPC::PlClient is for.  PlRPC works by 
defining a set of methods that may be executed by the client.

%prep
%setup -q -n PlRPC
%patch0 -p1

%build
%{?scl:scl enable %{scl} "}
%{__perl} Makefile.PL INSTALLDIRS=vendor
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
%doc ChangeLog README 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Mon Mar 11 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.2020-1
- SCL package - initial import
