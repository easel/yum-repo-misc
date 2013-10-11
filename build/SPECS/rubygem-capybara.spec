%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name capybara
%global rubyabi 1.9.1

Summary: Capybara aims to simplify the process of integration testing Rack applications, such as Rails, Sinatra or Merb
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.1.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/jnicklas/capybara
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems) 
Requires: %{?scl_prefix}ruby >= 1.9.3
Requires: %{?scl_prefix}rubygem(nokogiri) >= 1.3.3
Requires: %{?scl_prefix}rubygem(mime-types) >= 1.16
Requires: %{?scl_prefix}rubygem(rack) >= 1.0.0
Requires: %{?scl_prefix}rubygem(rack-test) >= 0.5.4
Requires: %{?scl_prefix}rubygem(xpath) => 2.0
Requires: %{?scl_prefix}rubygem(xpath) < 3
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel 
BuildRequires: %{?scl_prefix}ruby >= 1.9.3
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Capybara is an integration testing tool for rack based web applications. It
simulates how a user would interact with a website


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
%dir %{gem_instdir}/spec
%dir %{gem_instdir}/spec/fixtures
%dir %{gem_instdir}/spec/rspec
%{gem_instdir}/*
%{gem_instdir}/spec/*
%{gem_instdir}/spec/fixtures/*
%{gem_instdir}/spec/rspec/*
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Tue Apr 09 2013 Adam Miller <admiller@redhat.com> - 2.1.0-1
- Initial package

