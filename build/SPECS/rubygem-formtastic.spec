%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name formtastic
%global rubyabi 1.9.1

Summary: A Rails form builder plugin/gem
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 1.2.4
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/justinfrench/formtastic/tree/master
Source0: %{gem_name}-%{version}.gem
Requires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl:%scl_prefix}ruby
Requires: %{?scl:%scl_prefix}rubygems
Requires: %{?scl:%scl_prefix}rubygem(activesupport) >= 2.3.7
Requires: %{?scl:%scl_prefix}rubygem(actionpack) >= 2.3.7
Requires: %{?scl:%scl_prefix}rubygem(i18n) => 0.4
BuildRequires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}ruby 
BuildRequires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A Rails form builder plugin/gem with semantically rich and accessible markup


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
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/README.textile
%dir %{gem_instdir}
%{gem_instdir}/generators
%{gem_instdir}/rails
%{gem_instdir}/*.rb
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Thu Nov 08 2012 Thomas A. McGonagle <mcgonagle@redhat.com> - 1.2.4-2
- Release bump for OpenShift Enterprise Release

* Tue Sep 11 2012 Troy Dawson <tdawson@redhat.com> - 1.2.4-1
- updated to newer version

* Fri Aug 31 2012 Troy Dawson <tdawson@redhat.com> - 1.2.3-5
- Packaged to work with SCL
- Initial package
