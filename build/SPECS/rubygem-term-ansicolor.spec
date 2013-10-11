%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name term-ansicolor
%global rubyabi 1.9.1

Summary: Ruby library that colors strings using ANSI escape sequences
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 1.0.7
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://flori.github.com/term-ansicolor
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl:%scl_prefix}ruby
Requires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}ruby 
BuildRequires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Small Ruby library that colors strings using ANSI escape sequences.

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

# cleanup
rm -f %{buildroot}%{gem_instdir}/.gitignore
rm -f %{buildroot}%{gem_instdir}/.travis.yml

%files
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/doc-main.txt
%doc %{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/VERSION
%doc %{gem_instdir}/examples
%dir %{gem_instdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/*.rb
%{gem_instdir}/tests
%{_bindir}/cdiff
%{_bindir}/decolor
%{gem_instdir}/bin
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%changelog
* Tue Feb 26 2013 Troy Dawson <tdawson@redhat.com> - 1.0.7-2
- Rebuild to pull in fixes for Fix CVE-2013-0256

* Fri Aug 31 2012 Troy Dawson <tdawson@redhat.com> - 1.0.7-1
- Packaged to work with SCL
- Initial package
