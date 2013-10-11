%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name cucumber
%global rubyabi 1.9.1

Summary: cucumber-1.2.1
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 1.2.1
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://cukes.info
Source0: %{gem_name}-%{version}.gem
Requires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl:%scl_prefix}ruby
Requires: %{?scl:%scl_prefix}rubygems
Requires: %{?scl:%scl_prefix}rubygem(gherkin) => 2.11.0
Requires: %{?scl:%scl_prefix}rubygem(term-ansicolor) => 1.0.5
Requires: %{?scl:%scl_prefix}rubygem(builder) => 2.1.2
Requires: %{?scl:%scl_prefix}rubygem(diff-lcs) => 1.1.3
Requires: %{?scl:%scl_prefix}rubygem(json) => 1.4.6
BuildRequires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}ruby 
BuildRequires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}


%description
Behaviour Driven Development with elegance and joy


%prep
%{?scl:scl enable %scl "}
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}


%build
mkdir -p ./%{gem_dir}

%{?scl:scl enable %scl - << \EOF}
export LANG="en_US.UTF-8"
gem build %{gem_name}.gemspec
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --bindir ./%{_bindir} \
        --force \
        --rdoc \
        %{gem_name}-%{version}.gem
export LANG="C"
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

# Cleanup cruft
rm -f %{buildroot}%{gem_instdir}/.gitattributes
rm -f %{buildroot}%{gem_instdir}/.gitignore
rm -f %{buildroot}%{gem_instdir}/.rspec
rm -f %{buildroot}%{gem_instdir}/.rvmrc
rm -f %{buildroot}%{gem_instdir}/.travis.yml


%files
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/Gemfile
%dir %{gem_instdir}
%{_bindir}/cucumber
%{gem_instdir}/bin
%{gem_instdir}/features
%{gem_instdir}/legacy_features
%{gem_instdir}/gem_tasks
%{gem_instdir}/fixtures
%{gem_instdir}/spec
%{gem_instdir}/cucumber.yml
%{gem_instdir}/cucumber.gemspec
%{gem_instdir}/Rakefile
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}


%changelog
* Tue Feb 26 2013 Troy Dawson <tdawson@redhat.com> - 1.2.1-2
- Rebuild to pull in fixes for Fix CVE-2013-0256

* Fri Sep 29 2012 Wesley Hearn <whearn@redhat.com> - 1.2.1-1
- Bumped to 1.2.1

* Fri Aug 31 2012 Troy Dawson <tdawson@redhat.com>  - 0.9.0-5
- Packaged to work with SCL
- Initial package
