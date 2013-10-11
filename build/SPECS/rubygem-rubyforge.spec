%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name rubyforge
%global rubyabi 1.9.1

Summary: A script which automates a limited set of rubyforge operations
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 2.0.4
Release: 8%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://codeforpeople.rubyforge.org/rubyforge/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl:%scl_prefix}ruby
Requires: %{?scl:%scl_prefix}rubygems
Requires: %{?scl:%scl_prefix}rubygem(json_pure) >= 1.1.7
BuildRequires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}ruby 
BuildRequires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A script which automates a limited set of rubyforge operations.
* Run 'rubyforge help' for complete usage.
* Setup: For first time users AND upgrades to 0.4.0:
* rubyforge setup (deletes your username and password, so run sparingly!)
* edit ~/.rubyforge/user-config.yml
* rubyforge config
* For all rubyforge upgrades, run 'rubyforge config' to ensure you have
latest.

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

# If there were programs installed:
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}

find %{buildroot}%{_bindir} -type f | xargs chmod a+x

# Change from /usr/bin/ruby to /usr/bin/env ruby
find %{buildroot} -type f | \
  xargs sed -i -e 's"^#!/usr/bin/ruby"#!/usr/bin/env ruby"'

%files
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.txt
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/test
%dir %{gem_instdir}
%{_bindir}/rubyforge
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%changelog
* Fri Aug 31 2012 Troy Dawson <tdawson@redhat.com> - 2.0.4-8
- Packaged to work with SCL
- Initial package
