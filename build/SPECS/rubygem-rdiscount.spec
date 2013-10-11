%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name rdiscount
%global rubyabi 1.9.1

Summary: Fast Implementation of Gruber's Markdown in C
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 1.6.8
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/rtomayko/rdiscount
Source0: %{gem_name}-%{version}.gem
Requires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl:%scl_prefix}ruby
Requires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}ruby
BuildRequires: %{?scl:%scl_prefix}ruby-devel
BuildRequires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
Provides: %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Fast Implementation of Gruber's Markdown in C


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
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man7
mv ./%{gem_instdir}/man/rdiscount.1 %{buildroot}%{_mandir}/man1
mv ./%{gem_instdir}/man/markdown.7 %{buildroot}%{_mandir}/man7
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

# If there were programs installed:
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}

find %{buildroot}%{_bindir} -type f | xargs chmod a+x

# Change from /usr/bin/ruby to /usr/bin/env ruby
find %{buildroot} -type f | \
  xargs sed -i -e 's"^#!/usr/bin/ruby"#!/usr/bin/env ruby"'

mkdir -p %{buildroot}%{gem_extdir}/lib
# TODO: move the extensions
mv %{buildroot}%{gem_instdir}/lib/rdiscount.so %{buildroot}%{gem_extdir}/lib/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/ext

%files
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/README.markdown
%dir %{gem_instdir}
%{_bindir}/rdiscount
%{gem_instdir}/bin
%{gem_libdir}
%{gem_extdir}
%{gem_cache}
%{gem_spec}
%{_mandir}/man1/rdiscount.1.gz
%{_mandir}/man7/markdown.7.gz

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/BUILDING
%doc %{gem_instdir}/Rakefile
%{gem_instdir}/man
%{gem_instdir}/test
%{gem_instdir}/rdiscount.gemspec

%changelog
* Fri Sep 28 2012 Adam Miller <admiller@redhat.com> - 1.6.8-2
- Release bump for rebuild into both i386 and x86_64

* Tue Sep 11 2012 Troy Dawson <tdawson@redhat.com> - 1.6.8-1
- updated to newer version

* Fri Aug 31 2012 Troy Dawson <tdawson@redhat.com> - 1.6.3.2-6
- Packaged to work with SCL
- Initial package
