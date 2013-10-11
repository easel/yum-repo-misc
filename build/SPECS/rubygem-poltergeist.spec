# Generated from poltergeist-1.1.0.gem by gem2rpm -*- rhel6.scl.spec -*-
%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name poltergeist
%global rubyabi 1.9.1

Summary:       PhantomJS driver for Capybara
Name:          %{?scl:%scl_prefix}rubygem-%{gem_name}
Version:       1.2.0
Release:       1%{?dist}
Group:         Development/Languages
License:       MIT
URL:           http://github.com/jonleighton/poltergeist
Source0:       http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:      %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
Requires:      %{?scl:%scl_prefix}ruby(rubygems) 
Requires:      %{?scl:%scl_prefix}rubygem(capybara) => 2.0
Requires:      %{?scl:%scl_prefix}rubygem(capybara) < 3
Requires:      %{?scl:%scl_prefix}rubygem(capybara) >= 2.0.1
Requires:      %{?scl:%scl_prefix}rubygem(http_parser.rb) => 0.5.3
Requires:      %{?scl:%scl_prefix}rubygem(http_parser.rb) < 0.6
Requires:      %{?scl:%scl_prefix}rubygem(faye-websocket) => 0.4
Requires:      %{?scl:%scl_prefix}rubygem(faye-websocket) < 1
Requires:      %{?scl:%scl_prefix}rubygem(faye-websocket) >= 0.4.4
BuildRequires: %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
BuildArch:     noarch
Provides:      %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
PhantomJS driver for Capybara


%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}
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

# Remove build leftovers.
rm -rf %{buildroot}%{gem_instdir}/{.rvmrc,.document,.require_paths,.gitignore,.travis.yml,.rspec,.gemtest,.yard*}

%files
%doc %{gem_instdir}/[A-Z]*
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Wed Apr 10 2013 Troy Dawson <tdawson@redhat.com> - 1.1.0-1
- Initial package
