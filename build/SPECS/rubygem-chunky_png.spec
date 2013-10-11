%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name chunky_png
%global rubyabi 1.9.1

Summary: Pure ruby library for read/write, chunk-level access to PNG files
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 1.2.6
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://wiki.github.com/wvanbergen/chunky_png
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
This pure Ruby library can read and write PNG images without depending on
an external  image library, like RMagick. It tries to be memory efficient
and reasonably fast.
It supports reading and writing all PNG variants that are defined in the
specification,  with one limitation: only 8-bit color depth is supported.
It supports all transparency,  interlacing and filtering options the PNG
specifications allows. It can also read and  write textual metadata from
PNG files. Low-level read/write access to PNG chunks is also possible.
This library supports simple drawing on the image canvas and simple
operations like alpha composition and cropping. Finally, it can import
from and export to RMagick for  interoperability.
Also, have a look at OilyPNG at http://github.com/wvanbergen/oily_png.
OilyPNG is a  drop in mixin module that implements some of the ChunkyPNG
algorithms in C, which  provides a massive speed boost to encoding and decoding.

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

# cleanup
find %{buildroot} -iname .gitignore -exec rm -f {} \;
find %{buildroot} -iname .yardopts -exec rm -f {} \;
rm -f %{buildroot}%{gem_instdir}/.infinity_test
rm -f %{buildroot}%{gem_instdir}/.travis.yml

%files
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/BENCHMARKS.rdoc
%doc %{gem_instdir}/spec
%doc %{gem_instdir}/tasks
%doc %{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/benchmarks
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/Gemfile
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%changelog
* Tue Feb 26 2013 Troy Dawson <tdawson@redhat.com> - 1.2.6-2
- Rebuild to pull in fixes for Fix CVE-2013-0256

* Tue Sep 11 2012 Troy Dawson <tdawson@redhat.com> - 1.2.6-1
- updated to version 1.2.6

* Fri Aug 31 2012 Troy Dawson <tdawson@redhat.com> - 1.2.0-3
- Packaged to work with SCL
- Initial package
