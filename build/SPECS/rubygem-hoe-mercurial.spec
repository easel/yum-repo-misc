%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name hoe-mercurial
%global rubyabi 1.8

Summary:       A fork of the hoe-hg plugin
Name:          %{?scl:%scl_prefix}rubygem-%{gem_name}
Version:       1.4.0
Release:       1%{?dist}
Group:         Development/Ruby
License:       MIT
URL:           http://bitbucket.org/ged/hoe-mercurial
Source0:       http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires:      %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
Requires:      %{?scl:%scl_prefix}ruby(rubygems)
Requires:      %{?scl:%scl_prefix}rubygem(hoe)
Requires:      %{?scl:%scl_prefix}rubygem(rdoc)
BuildRequires: %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
BuildArch:     noarch
Provides:      %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This is a fork of the [hoe-hg](https://bitbucket.org/mml/hoe-hg) 
plugin. I forked it because I use quite a few additional Mercurial 
tasks for my development workflow than are provided by the original, 
and I thought they'd possibly be useful to someone else.
I've offered to push my changes back up to the original, but I gave
up waiting for a response.


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

gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
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

# We don't need those files anymore.
rm -rf %{buildroot}%{gem_instdir}/{.rvmrc,.document,.require_paths,.gitignore,.travis.yml,.yardoc}

%files
%doc %{gem_instdir}/[A-Z]*
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile

%changelog
* Tue Apr 09 2013 Troy Dawson <tdawson@redhat.com> - 1.4.0-1
- Initial package

