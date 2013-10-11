%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name addressable
%global rubyabi 1.9.1

Summary: URI Implementation
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 2.3.2
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://addressable.rubyforge.org/
Source0: %{gem_name}-%{version}.gem
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
Addressable is a replacement for the URI implementation that is part of
Ruby's standard library. It more closely conforms to the relevant RFCs and
adds support for IRIs and URI templates.


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

%files
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/CHANGELOG.md
%dir %{gem_instdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/tasks
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
# Ignoring the author's website packaged with the gem
%exclude %{gem_instdir}/website/
%doc %{gem_instdir}/CHANGELOG.md

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Gemfile

%changelog
* Tue Sep 11 2012 Troy Dawson <tdawson@redhat.com> - 2.3.2-1
- updated to version 2.3.2

* Fri Aug 31 2012 Troy Dawson <tdawson@redhat.com> - 2.2.6-2
- Packaged to work with SCL
- Initial package
