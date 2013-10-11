%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name gherkin
%global rubyabi 1.9.1

Summary: fast Gherkin lexer/parser
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 2.11.2
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/aslakhellesoy/gherkin
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl:%scl_prefix}ruby
Requires: %{?scl:%scl_prefix}rubygems
Requires: %{?scl:%scl_prefix}rubygem(trollop) => 1.16.2
Requires: %{?scl:%scl_prefix}rubygem(json) => 1.4.6
Requires: %{?scl:%scl_prefix}rubygem(term-ansicolor) => 1.0.5
BuildRequires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}ruby 
BuildRequires: %{?scl:%scl_prefix}ruby-devel
BuildRequires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
Provides: %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A fast Gherkin lexer/parser based on the Ragel State Machine Compiler.


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

# Change from /usr/bin/ruby to /usr/bin/env ruby
find %{buildroot} -type f | \
  xargs sed -i -e 's"^#!/usr/bin/ruby"#!/usr/bin/env ruby"'

mkdir -p %{buildroot}%{gem_extdir}/lib
# TODO: move the extensions
mv %{buildroot}%{gem_instdir}/lib/*.so %{buildroot}%{gem_extdir}/lib/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/ext

# Remove git files
rm -f %{buildroot}%{gem_instdir}/.gitattributes
rm -f %{buildroot}%{gem_instdir}/.mailmap
rm -f %{buildroot}%{gem_instdir}/.rspec
rm -f %{buildroot}%{gem_instdir}/.rvmrc
rm -f %{buildroot}%{gem_instdir}/.travis.yml
rm -f %{buildroot}%{gem_instdir}/.yardopts
rm -f %{buildroot}%{gem_instdir}/.rbenv-gemsets
rm -f %{buildroot}%{gem_instdir}/install_mingw_os_x.sh

%files
%doc %{gem_instdir}/features
%doc %{gem_instdir}/spec
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/cucumber.yml
%doc %{gem_instdir}/Gemfile
%dir %{gem_instdir}
%{gem_instdir}/ragel
%{gem_instdir}/js
%{gem_instdir}/gherkin.gemspec
%{gem_instdir}/build_native_gems.sh
%{gem_libdir}
%{gem_extdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/tasks
%{gem_instdir}/examples

%changelog
* Sat Sep 29 2012 Troy Dawson <tdawson@redhat.com> - 2.11.2-2
- Release bump for rebuild into both i386 and x86_64

* Fri Aug 31 2012 Troy Dawson <tdawson@redhat.com> - 2.11.2-1
- Packaged to work with SCL
- Initial package
