%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name eventmachine
%global rubyabi 1.8

Summary:       Ruby EventMachine library
Name:          %{?scl:%scl_prefix}rubygem-%{gem_name}
Version:       1.0.3
Release:       1%{?dist}
Group:         Development/Ruby
License:       Ruby or GPL2
URL:           http://rubyeventmachine.com
Source0:       http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires:      %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
Requires:      %{?scl:%scl_prefix}ruby(rubygems)
Requires:      %{?scl:%scl_prefix}rubygem(rake-compiler)
Requires:      %{?scl:%scl_prefix}rubygem(yard)
Requires:      %{?scl:%scl_prefix}rubygem(bluecloth)
BuildRequires: %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}ruby-devel
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
Provides:      %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs
to specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal
of EventMachine is to enable programs to easily interface with other programs
using TCP/IP, especially if custom protocols are required.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%{?scl:scl enable %scl "}
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p ./%{gem_dir}
%{?scl:scl enable %scl - << \EOF}
gem build %{gem_name}.gemspec

gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --force \
        --rdoc \
        %{gem_name}-%{version}.gem
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

# Change from /usr/bin/ruby to /usr/bin/env ruby
find %{buildroot} -type f | \
  xargs sed -i -e 's"^#!/usr/bin/ruby"#!/usr/bin/env ruby"'

mkdir -p %{buildroot}%{gem_extdir}/lib/%{name}/
mv %{buildroot}%{gem_instdir}/ext/rubyeventmachine.so %{buildroot}%{gem_extdir}/lib/


# We don't need those files anymore.
rm -rf %{buildroot}%{gem_instdir}/{.rvmrc,.document,.require_paths,.gitignore,.travis.yml,.yardo*}
rm -rf $RPM_BUILD_ROOT%{gem_instdir}/ext/
rm -rf $RPM_BUILD_ROOT%{gem_instdir}/java/
rm -rf %{buildroot}%{gem_instdir}/*.gemspec

%files
%doc %{gem_instdir}/[A-Z]*
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/docs
%{gem_instdir}/examples
%{gem_instdir}/rakelib
%{gem_instdir}/tests

%changelog
* Tue Apr 09 2013 Troy Dawson <tdawson@redhat.com> - 1.0.3-1
- Initial package

