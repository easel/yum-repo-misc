%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name highline
%global rubyabi 1.9.1

Summary: HighLine is a high-level command-line IO library
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 1.6.16
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://highline.rubyforge.org
Source0: %{gem_name}-%{version}.gem
Requires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl:%scl_prefix}ruby
Requires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}ruby 
BuildRequires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A high-level IO library that provides validation, type conversion, and more
for command-line interfaces. HighLine also includes a complete menu system
that can crank out anything from simple list selection to complete shells with
just minutes of work.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

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
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --bindir ./%{_bindir} \
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


%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{gem_instdir}/examples
%{gem_instdir}/setup.rb

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/INSTALL
%doc %{gem_instdir}/TODO
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/AUTHORS
%doc %{gem_instdir}/COPYING
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/site
%{gem_instdir}/doc
%{gem_instdir}/*gemspec
%{gem_instdir}/.gitignore

%changelog
* Fri Aug 31 2012 Troy Dawson <tdawson@redhat.com>  - 1.5.1-5
- Packaged to work with SCL
- Initial package
