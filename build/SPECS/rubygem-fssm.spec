%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
# Generated from fssm-0.2.8.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fssm
%global rubyabi 1.9.1

Summary: File System State Monitor
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 0.2.8.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/ttilley/fssm
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl:%scl_prefix}ruby(rubygems) 
BuildRequires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}rubygems-devel 
BuildRequires: %{?scl:%scl_prefix}rubygem(rspec)
BuildArch: noarch
Provides: %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
The File System State Monitor keeps track of the state of any number of paths
and will fire events when said state changes (create/update/delete). FSSM
supports using FSEvents on MacOS, Inotify on GNU/Linux, and polling anywhere
else.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl:%scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# kill bundler
sed -i '5d' spec/spec_helper.rb
%{?scl:scl enable %scl "}
rspec spec
%{?scl:"}

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/ext
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/example.rb
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/profile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.8.1-1
- Initial package for scl
