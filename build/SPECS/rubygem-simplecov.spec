%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name simplecov

Summary:       Code coverage for Ruby 1.9 with a powerful configuration library and automatic merging of coverage across test suites
Name:          %{?scl:%scl_prefix}rubygem-%{gem_name}
Version:       0.6.4
Release:       2%{?dist}
Group:         Development/Languages
License:       GPLv2+ or Ruby
URL:           http://github.com/colszowka/simplecov
Source0:       http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:      %{?scl:%scl_prefix}ruby
Requires:      %{?scl:%scl_prefix}rubygems
Requires:      %{?scl:%scl_prefix}rubygem(multi_json) => 1.0
Requires:      %{?scl:%scl_prefix}rubygem(simplecov-html) => 0.5.3
BuildRequires: %{?scl:%scl_prefix}ruby 
BuildRequires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
BuildArch:     noarch
Provides:      %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Code coverage for Ruby 1.9 with a powerful configuration library and automatic
merging of coverage across test suites


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

#cleanup
rm -f %{buildroot}%{gem_instdir}/.gitignore
rm -f %{buildroot}%{gem_instdir}/.travis.yml
rm -f %{buildroot}%{gem_instdir}/simplecov.gemspec

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/Appraisals
%{gem_instdir}/CHANGELOG.md
%{gem_instdir}/README.md
%{gem_instdir}/cucumber.yml
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/features
%{gem_instdir}/gemfiles
%{gem_instdir}/test
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Tue Aug 28 2012 Troy Dawson <tdawson@redhat.com> - 1.2.1-2
- Packaged to work with SCL

* Mon Aug 27 2012 Troy Dawson <tdawson@redhat.com> - 0.6.4-1
- Initial package
