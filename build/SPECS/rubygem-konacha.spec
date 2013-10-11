%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name konacha
%global rubyabi 1.9.1

Summary: Unit-test your Rails JavaScript with the mocha test framework and chai assertion library
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.6.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/jfirebaugh/konacha
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems) 
Requires: %{?scl_prefix}ruby 
Requires: %{?scl_prefix}rubygem(railties) >= 3.1
Requires: %{?scl_prefix}rubygem(railties) < 5
Requires: %{?scl_prefix}rubygem(actionpack) >= 3.1
Requires: %{?scl_prefix}rubygem(actionpack) < 5
Requires: %{?scl_prefix}rubygem(sprockets) 
Requires: %{?scl_prefix}rubygem(capybara) 
Requires: %{?scl_prefix}rubygem(colorize) 
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel 
BuildRequires: %{?scl_prefix}ruby 
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Konacha is a Rails engine that allows you to test your JavaScript with the
mocha test framework and chai assertion library.
It is similar to Jasmine and Evergreen, but does not attempt to be framework
agnostic. By sticking with Rails, Konacha can take full advantage of features
such as
the asset pipeline and engines.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/*
%exclude %{gem_cache}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.gitmodules
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Tue Apr 09 2013 Adam Miller <admiller@redhat.com> - 2.6.0-1
- Initial package

