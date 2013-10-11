%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name ci_reporter
%global rubyabi 1.9.1

Summary: CI::Reporter allows you to generate reams of XML for use with continuous integration systems
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 1.7.2
Release: 3%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://caldersphere.rubyforge.org/ci_reporter
Source0: %{gem_name}-%{version}.gem
Requires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl:%scl_prefix}ruby
Requires: %{?scl:%scl_prefix}rubygems
Requires: %{?scl:%scl_prefix}rubygem(builder) >= 2.1.2
BuildRequires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}ruby 
BuildRequires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
CI::Reporter is an add-on to Test::Unit, RSpec and Cucumber that allows you to
generate XML reports of your test, spec and/or feature runs. The resulting
files can be read by a continuous integration system that understands Ant's
JUnit report XML format, thus allowing your CI system to track test/spec
successes and failures.

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

rm -f %{buildroot}%{gem_instdir}/.gemtest
rm -f %{buildroot}%{gem_instdir}/.travis.yml
rm -f %{buildroot}%{gem_instdir}/Gemfile
rm -f %{buildroot}%{gem_instdir}/Gemfile.lock
rm -f %{buildroot}%{gem_instdir}/ci_reporter.gemspec

%files
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.rdoc
%dir %{gem_instdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/stub.rake
%{gem_instdir}/spec
%{gem_instdir}/tasks
%{gem_instdir}/acceptance
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%changelog
* Tue Feb 26 2013 Troy Dawson <tdawson@redhat.com> - 1.7.2-3
- Rebuild to pull in fixes for Fix CVE-2013-0256

* Tue Sep 11 2012 Troy Dawson <tdawson@redhat.com> - 1.7.2-1
- updated to version 1.7.2

* Fri Aug 31 2012 Troy Dawson <tdawson@redhat.com> - 1.7.0-2
- Packaged to work with SCL
- Initial package
