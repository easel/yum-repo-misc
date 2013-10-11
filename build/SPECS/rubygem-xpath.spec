%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name xpath
%global rubyabi 1.9.1

Summary: Generate XPath expressions from Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.0.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/jnicklas/xpath
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems) 
Requires: %{?scl_prefix}ruby 
Requires: %{?scl_prefix}rubygem(nokogiri) => 1.3
Requires: %{?scl_prefix}rubygem(nokogiri) < 2
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel 
BuildRequires: %{?scl_prefix}ruby 
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
XPath is a Ruby DSL for generating XPath expressions


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
%{gem_instdir}/spec
%{gem_instdir}/spec/fixtures
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Apr 09 2013 Adam Miller <admiller@redhat.com> - 2.0.0-1
- Initial package

