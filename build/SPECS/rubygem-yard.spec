%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name yard
%global rubyabi 1.9.1

Summary: Documentation tool for consistent and usable documentation in Ruby
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 0.7.2
Release: 4%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://yardoc.org
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
YARD is a documentation generation tool for the Ruby programming language.
It enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.

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
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{_bindir}/yard
%{_bindir}/yardoc
%{_bindir}/yri
%{gem_instdir}/.yardopts
%{gem_instdir}/bin
%{gem_instdir}/benchmarks
%{gem_instdir}/spec
%{gem_instdir}/templates
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_docdir}
%doc %{gem_instdir}/LEGAL
%{gem_instdir}/ChangeLog
%{gem_instdir}/docs
%{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Tue Feb 26 2013 Troy Dawson <tdawson@redhat.com> - 0.7.2-4
- Rebuild to pull in fixes for Fix CVE-2013-0256

* Tue Sep 04 2012 Troy Dawson <tdawson@redhat.com> - 0.7.2-3
- Redid files to be in the same rpm as non-scl package

* Fri Aug 31 2012 Troy Dawson <tdawson@redhat.com> - 0.7.2-2
- Packaged to work with SCL
- Initial package
