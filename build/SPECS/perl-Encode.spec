%{?scl:%scl_package perl-Encode}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Encode
Version:        2.51
Release:        1%{?dist}
Summary:        Character encodings in Perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Encode/
Source0:        http://www.cpan.org/authors/id/D/DA/DANKOGAI/Encode-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(bytes)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
# Filter::Util::Call is optional
BuildRequires:  %{?scl_prefix}perl(Getopt::Long)
# I18N::Langinfo is optional
BuildRequires:  %{?scl_prefix}perl(MIME::Base64)
# PerlIO::encoding is optional
BuildRequires:  %{?scl_prefix}perl(re)
# Storable is optional
BuildRequires:  %{?scl_prefix}perl(utf8)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# Tests:
BuildRequires:  %{?scl_prefix}perl(charnames)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(IO::Select)
BuildRequires:  %{?scl_prefix}perl(IPC::Open3)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Encode::ConfigLocal|MY\\)

%{?scl:
%filter_from_provides /\.so()/d
%filter_from_provides /perl(\(Encode::ConfigLocal\|MY\))/d
%filter_setup
}

%description
The Encode module provides the interface between Perl strings and the rest
of the system. Perl strings are sequences of characters.

# To mirror files from perl-devel (bug #456534)
# Keep architecture specific because files go into vendorarch
%package devel
Summary:        Perl Encode Module Generator
Group:          Development/Libraries
Requires:       %{?scl_prefix}%{pkg_name}%{?_isa} = %{version}-%{release}
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl-devel
Requires:       %{?scl_prefix}perl(Encode)

%description devel
enc2xs builds a Perl extension for use by Encode from either Unicode Character
Mapping files (.ucm) or Tcl Encoding Files (.enc). You can use enc2xs to add
your own encoding to perl. No knowledge of XS is necessary.


%prep
%setup -q -n Encode-%{version}

%build
# Additional scripts can be installed by appending MORE_SCRIPTS, UCM files by
# INSTALL_UCM.
%{?scl:scl enable %{scl} '}
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{?scl:'}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc AUTHORS Changes README
%{_bindir}/piconv
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Encode*
%exclude %{perl_vendorarch}/Encode/*.e2x
%exclude %{perl_vendorarch}/Encode/encode.h
%{perl_vendorarch}/encoding.pm
%{_mandir}/man1/piconv.*
%{_mandir}/man3/*

%files devel
%{_bindir}/enc2xs
%{_mandir}/man1/enc2xs.*
%{perl_vendorarch}/Encode/*.e2x
%{perl_vendorarch}/Encode/encode.h

%changelog
* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.51-1
- 2.51 bump

* Wed Apr 03 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.49-1
- SCL package - initial import
