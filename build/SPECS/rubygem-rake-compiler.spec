%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name rake-compiler
%global rubyabi 1.8

Summary:       Rake-based Ruby Extension (C, Java) task generator.
Name:          %{?scl:%scl_prefix}rubygem-%{gem_name}
Version:       0.8.3
Release:       1%{?dist}
Group:         Development/Ruby
License:       MIT
URL:           http://github.com/luislavena/rake-compiler
Source0:       http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires:      %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
Requires:      %{?scl:%scl_prefix}ruby(rubygems)
Requires:      %{?scl:%scl_prefix}rubygem(rake)
Requires:      %{?scl:%scl_prefix}rubygem(rspec)
Requires:      %{?scl:%scl_prefix}rubygem(cucumber)
BuildRequires: %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
BuildArch:     noarch
Provides:      %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Provide a standard and simplified way to build and package
Ruby extensions (C, Java) using Rake as glue.


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

# If there were programs installed:
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}

# We don't need those files anymore.
rm -rf %{buildroot}%{gem_instdir}/{.rvmrc,.document,.require_paths,.gitignore,.travis.yml,.yardoc}

%files
%doc %{gem_instdir}/[A-Z]*
%dir %{gem_instdir}
%{_bindir}
%{gem_instdir}/bin
%{gem_instdir}/features
%{gem_instdir}/spec
%{gem_instdir}/tasks
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/cucumber.yml


%changelog
* Tue Apr 09 2013 Troy Dawson <tdawson@redhat.com> - 0.8.3-1
- Initial package

