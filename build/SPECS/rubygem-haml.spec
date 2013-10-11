# Generated from haml-4.0.3.gem by gem2rpm -*- rhel6.scl.spec -*-
%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name haml
%global rubyabi 1.9.1

Summary:       An elegant, structured XHTML/XML templating engine
Name:          %{?scl_prefix}rubygem-%{gem_name}
Version:       4.0.3
Release:       2%{?dist}
Group:         Development/Languages
License:       MIT
URL:           http://haml.info/
Source0:       http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:      %{?scl_prefix}ruby(abi) >= %{rubyabi}
Requires:      %{?scl_prefix}ruby(rubygems) 
Requires:      %{?scl_prefix}rubygem(tilt) 
BuildRequires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch:     noarch
Provides:      %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Haml (HTML Abstraction Markup Language) is a layer on top of 
XHTML or XML that's designed to express the structure of XHTML
 or XML documents in a non-repetitive, elegant, easy way,
using indentation rather than closing tags
and allowing Ruby to be embedded with ease.
It was originally envisioned as a plugin for Ruby on Rails,
but it can function as a stand-alone templating engine.

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
         --bindir .%{_bindir} \
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

mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Remove build leftovers.
rm -rf %{buildroot}%{gem_instdir}/{.rvmrc,.document,.require_paths,.gitignore,.travis.yml,.rspec,.gemtest,.yard*}

%files
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/FAQ.md
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/REFERENCE.md
%dir %{gem_instdir}
%{_bindir}/haml
%{gem_instdir}/bin
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%changelog
* Tue Sep 17 2013 Troy Dawson <tdawson@redhat.com> - 4.0.3-2
- Update to latest version - (#1008835)

* Tue Feb 26 2013 Troy Dawson <tdawson@redhat.com> - 3.1.7-2
- Rebuild to pull in fixes for Fix CVE-2013-0256

* Tue Sep 11 2012 Troy Dawson <tdawson@redhat.com> - 3.1.7-1
- updated to newer version

* Fri Aug 31 2012 Troy Dawson <tdawson@redhat.com> - 3.1.2-4
- Packaged to work with SCL
- Initial package
