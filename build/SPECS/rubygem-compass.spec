%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name compass
%global rubyabi 1.9.1

Summary: A Real Stylesheet Framework
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 0.12.2
Release: 3%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://compass-style.org
Source0: %{gem_name}-%{version}.gem
Requires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl:%scl_prefix}ruby
Requires: %{?scl:%scl_prefix}rubygems
Requires: %{?scl:%scl_prefix}rubygem(sass) => 3.1
Requires: %{?scl:%scl_prefix}rubygem(chunky_png) => 1.2
Requires: %{?scl:%scl_prefix}rubygem(fssm) >= 0.2.7
BuildRequires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}ruby 
BuildRequires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Compass is a Sass-based Stylesheet Framework that streamlines the creation and
maintainance of CSS.

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
%doc %{gem_instdir}/LICENSE.markdown
%doc %{gem_instdir}/README.markdown
%doc %{gem_instdir}/VERSION.yml
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/test
%doc %{gem_instdir}/features
%dir %{gem_instdir}
%{_bindir}/compass
%{gem_instdir}/bin
%{gem_instdir}/frameworks
%{gem_instdir}/Rakefile
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%changelog
* Tue Feb 26 2013 Troy Dawson <tdawson@redhat.com> - 0.12.2-3
- Rebuild to pull in fixes for Fix CVE-2013-0256

* Tue Sep 11 2012 Troy Dawson <tdawson@redhat.com> - 0.12.2-2
- updated to version 0.12.2

* Fri Aug 31 2012 Troy Dawson <tdawson@redhat.com> - 0.11.5-3
- Packaged to work with SCL
- Initial package
