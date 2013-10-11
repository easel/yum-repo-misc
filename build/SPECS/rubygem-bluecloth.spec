%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name bluecloth
%global rubyabi 1.8

Summary:       A text-to-HTML conversion tool for web writers
Name:          %{?scl:%scl_prefix}rubygem-%{gem_name}
Version:       2.2.0
Release:       1%{?dist}
Group:         Development/Ruby
License:       MIT
URL:           http://deveiate.org/projects/BlueCloth
Source0:       http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires:      %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
Requires:      %{?scl:%scl_prefix}ruby(rubygems)
Requires:      %{?scl:%scl_prefix}rubygem(hoe-mercurial)
Requires:      %{?scl:%scl_prefix}rubygem(hoe-highline)
Requires:      %{?scl:%scl_prefix}rubygem(tidy-ext)
Requires:      %{?scl:%scl_prefix}rubygem(rake-compiler)
Requires:      %{?scl:%scl_prefix}rubygem(rspec)
Requires:      %{?scl:%scl_prefix}rubygem(hoe)
BuildRequires: %{?scl:%scl_prefix}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl:%scl_prefix}ruby-devel
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
Provides:      %{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}

%description
BlueCloth is a Ruby implementation of John Gruber's
Markdown[http://daringfireball.net/projects/markdown/], a text-to-HTML
conversion tool for web writers. To quote from the project page: Markdown
allows you to write using an easy-to-read, easy-to-write plain text format,
then convert it to structurally valid XHTML (or HTML).
It borrows a naming convention and several helpings of interface from
{Redcloth}[http://redcloth.org/], Why the Lucky Stiff's processor for a
similar text-to-HTML conversion syntax called
Textile[http://www.textism.com/tools/textile/].
BlueCloth 2 is a complete rewrite using David Parsons'
Discount[http://www.pell.portland.or.us/~orc/Code/discount/] library, a C
implementation of Markdown. I rewrote it using the extension for speed and
accuracy; the original BlueCloth was a straight port from the Perl version
that I wrote in a few days for my own use just to avoid having to shell out to
Markdown.pl, and it was quite buggy and slow. I apologize to all the good
people that sent me patches for it that were never released.
Note that the new gem is called 'bluecloth' and the old one 'BlueCloth'. 


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
#find %{buildroot} -type f | \
#  xargs sed -i -e 's"^#!/usr/bin/ruby"#!/usr/bin/env ruby"'

mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{gem_extdir}/lib/%{name}/
mv %{buildroot}%{gem_instdir}/ext/bluecloth_ext.so %{buildroot}%{gem_extdir}/lib/

# We don't need those files anymore.
rm -rf %{buildroot}%{gem_instdir}/{.rvmrc,.document,.require_paths,.gitignore,.travis.yml,.yardoc,.rspec,.gemtest}
rm -rf $RPM_BUILD_ROOT%{gem_instdir}/ext/

%files
%doc %{gem_instdir}/[A-Z]*
%dir %{gem_instdir}
%{_bindir}
%{gem_instdir}/bin
%{gem_instdir}/spec
%{gem_instdir}/bluecloth.1.pod
%{gem_extdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/man
%{gem_instdir}/Rakefile

%changelog
* Tue Apr 09 2013 Troy Dawson <tdawson@redhat.com> - 2.2.0-1
- Initial package

