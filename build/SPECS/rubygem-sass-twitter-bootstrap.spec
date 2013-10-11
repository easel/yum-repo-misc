# Generated from sass-twitter-bootstrap-2.0.1.gem by gem2rpm -*- rhel6.scl.spec -*-
%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name sass-twitter-bootstrap
%global rubyabi 1.9.1

Summary:       Gemification of the Twitter Bootstrap
Name:          %{?scl:%scl_prefix}rubygem-%{gem_name}
Version:       2.0.1
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           http://github.com/wadetandy/sass-twitter-bootstrap
Source0:       %{gem_name}-%{version}.gem
Requires:      %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
Requires:      %{?scl:%scl_prefix}ruby(rubygems) 
Requires:      %{?scl:%scl_prefix}rubygem(sass) 
Requires:      %{?scl:%scl_prefix}rubygem(railties) 
BuildRequires: %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
BuildArch:     noarch
Provides:      %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A Rails 2 and 3 compatible gem for John Long's Sass conversion of the Twitter Bootstrap.

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
%dir %{gem_instdir}
%{gem_instdir}/vendor
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Tue Jul 16 2013 Troy Dawson <tdawson@redhat.com> - 2.0.1-1
- Initial package
