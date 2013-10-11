%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name yajl-ruby
%global rubyabi 1.8

Summary:       Ruby C bindings to the Yajl JSON stream-based parser library.
Name:          %{?scl:%scl_prefix}rubygem-%{gem_name}
Version:       1.1.0
Release:       1%{?dist}
Group:         Development/Ruby
License:       MIT
URL:           http://github.com/brianmario/yajl-ruby
Source0:       http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires:      %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
Requires:      %{?scl:%scl_prefix}ruby(rubygems)
Requires:      %{?scl:%scl_prefix}rubygem(rake-compiler)
Requires:      %{?scl:%scl_prefix}rubygem(rspec)
Requires:      %{?scl:%scl_prefix}rubygem(activesupport)
Requires:      %{?scl:%scl_prefix}rubygem(json)
BuildRequires: %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}ruby-devel
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
Provides:      %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Ruby C bindings to the excellent Yajl JSON stream-based parser library.


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
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
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
mv %{buildroot}%{gem_instdir}/ext/yajl/yajl.so %{buildroot}%{gem_extdir}/lib/%{name}/

# We don't need those files anymore.
rm -rf %{buildroot}%{gem_instdir}/{.rvmrc,.document,.require_paths,.gitignore,.travis.yml,.yardoc,.rspec}
rm -rf $RPM_BUILD_ROOT%{gem_instdir}/ext/
rm -rf %{buildroot}%{gem_instdir}/*.gemspec

%files
%doc %{gem_instdir}/[A-Z]*
%dir %{gem_instdir}
%{gem_instdir}/tasks
%{gem_instdir}/spec
%{gem_libdir}
%{gem_extdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/benchmark
%{gem_instdir}/examples

%changelog
* Tue Apr 09 2013 Troy Dawson <tdawson@redhat.com> - 1.1.0-1
- Initial package

