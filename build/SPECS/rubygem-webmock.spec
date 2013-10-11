%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name webmock
%global rubyabi 1.9.1

Summary: Library for stubbing HTTP requests in Ruby
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 1.8.11
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/bblimke/webmock
Source0: %{gem_name}-%{version}.gem
Requires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl:%scl_prefix}ruby
Requires: %{?scl:%scl_prefix}rubygems
Requires: %{?scl:%scl_prefix}rubygem(addressable) => 2.2
Requires: %{?scl:%scl_prefix}rubygem(crack) >= 0.1.7
BuildRequires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}ruby 
BuildRequires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
WebMock allows stubbing HTTP requests and setting expectations on HTTP
requests.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
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

# Cleanup git files
rm -f %{buildroot}%{gem_instdir}/.gitignore

%files
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{gem_instdir}/.rvmrc
%{gem_instdir}/.travis.yml
%{gem_instdir}/.rspec-tm
%{gem_instdir}/.rvmrc
%{gem_instdir}/.gemtest
%{gem_instdir}/spec
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/Guardfile
%doc %{gem_instdir}/test
%doc %{gem_instdir}/minitest
%doc %{gem_instdir}/webmock.gemspec

%files doc
%doc %{gem_docdir}

%changelog
* Tue Sep 04 2012 Troy Dawson <tdawson@redhat.com> - 1.6.4-3
- Redid files to be in the same rpm as non-scl package

* Fri Aug 31 2012 Troy Dawson <tdawson@redhat.com> - 1.6.4-2
- Packaged to work with SCL
- Initial package
