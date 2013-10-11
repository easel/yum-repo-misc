%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name faye-websocket
%global rubyabi 1.8

Summary:       Standards-compliant WebSocket server and client
Name:          %{?scl:%scl_prefix}rubygem-%{gem_name}
Version:       0.4.7
Release:       2%{?dist}
Group:         Development/Ruby
License:       MIT
URL:           http://github.com/faye/faye-websocket-ruby
Source0:       http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires:      %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
Requires:      %{?scl:%scl_prefix}ruby(rubygems)
Requires:      %{?scl:%scl_prefix}rubygem(eventmachine)
BuildRequires: %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}ruby-devel
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
Provides:      %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description

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
mv %{buildroot}%{gem_instdir}/ext/faye_websocket_mask/faye_websocket_mask.so %{buildroot}%{gem_extdir}/lib/%{name}/

# We don't need those files anymore.
rm -rf %{buildroot}%{gem_instdir}/{.rvmrc,.document,.require_paths,.gitignore,.travis.yml,.yardoc}
rm -rf $RPM_BUILD_ROOT%{gem_instdir}/ext/
rm -rf %{buildroot}%{gem_instdir}/*.gemspec

%files
%doc %{gem_instdir}/[A-Z]*
%dir %{gem_instdir}
%{gem_instdir}/spec
%{gem_libdir}
%{gem_extdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/examples

%changelog
* Wed Apr 10 2013 Troy Dawson <tdawson@redhat.com> - 0.4.7-2
- Fix dependancies

* Tue Apr 09 2013 Troy Dawson <tdawson@redhat.com> - 0.4.7-1
- Initial package

