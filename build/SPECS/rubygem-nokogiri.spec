%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
%global gem_name nokogiri


# Note for packager:
# Nokogiri 1.4.3.1 gem says that Nokogiri upstream will
# no longer support ruby 1.8.6 after 2010-08-01, so
# it seems that 1.4.3.1 is the last version for F-13 and below.

Summary:	An HTML, XML, SAX, and Reader parser
Name:		%{?scl:%scl_prefix}rubygem-%{gem_name}
Version:	1.5.2
Release:	4%{?dist}
Group:		Development/Languages
License:	MIT
URL:		http://nokogiri.rubyforge.org/nokogiri/
Source0:	http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
BuildRequires: %{?scl:%scl_prefix}ruby
BuildRequires: %{?scl:%scl_prefix}ruby-devel
BuildRequires: %{?scl:%scl_prefix}rubygems
BuildRequires: %{?scl:%scl_prefix}rubygems-devel
BuildRequires: %{?scl:%scl_prefix}rubygem(minitest)
##
## Others
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
Requires:	%{?scl:%scl_prefix}ruby
Requires:	%{?scl:%scl_prefix}rubygems
Provides:	%{?scl:%scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}

%description
Nokogiri parses and searches XML/HTML very quickly, and also has
correctly implemented CSS3 selector support as well as XPath support.

Nokogiri also features an Hpricot compatibility layer to help ease the change
to using correct CSS and XPath.

%if 0
%package	jruby
Summary:	JRuby support for %{name}
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description	jruby
This package contains JRuby support for %{name}.
%endif


%package	doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%package	-n %{?scl:%scl_prefix}ruby-%{gem_name}
Summary:	Non-Gem support package for %{gem_name}
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Provides:	%{?scl:%scl_prefix}ruby(%{gem_name}) = %{version}-%{release}

%description	-n %{?scl:%scl_prefix}ruby-%{gem_name}
This package provides non-Gem support for %{gem_name}.

%prep
%setup -q -T -c

mkdir -p ./%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %scl "}
gem install \
	--local \
	--install-dir ./%{gem_dir} \
	-V --force \
	%{SOURCE0}
%{?scl:"}

# Permission
chmod 0644 .%{gem_dir}/cache/%{gem_name}-%{version}.gem

# Remove precompiled Java .jar file
rm -f .%{gem_instdir}/lib/*.jar
# For now remove JRuby support
rm -rf .%{gem_instdir}/ext/java

find -type f -exec sed -i 's|^#!/usr/bin/ruby|^#!%{?scl:%_scl_root}/usr/bin/ruby|' "{}" \;

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}

# Remove backup file
find %{buildroot} -name \*.orig_\* | xargs rm -vf

# move arch dependent files to %%gem_extdir
mkdir -p %{buildroot}%{gem_extdir}/lib/%{gem_name}
mv %{buildroot}%{gem_instdir}/lib/%{gem_name}/*.so \
	%{buildroot}%{gem_extdir}/lib/%{gem_name}/

# move bin/ files
mkdir -p %{buildroot}%{_prefix}
mv -f %{buildroot}%{gem_dir}/bin %{buildroot}%{_prefix}

# remove all shebang
for f in $(find %{buildroot}%{gem_instdir} -name \*.rb)
do
	sed -i -e '/^#!/d' $f
	chmod 0644 $f
done

# cleanups
rm -rf %{buildroot}%{gem_instdir}/ext/%{gem_name}/
rm -rf %{buildroot}%{gem_instdir}/tmp/
rm -f %{buildroot}%{gem_instdir}/{.autotest,.require_paths,.gemtest}

%check
# Ah....
# test_exslt(TestXsltTransforms) [./test/test_xslt_transforms.rb:93]
# fails without TZ on sparc
export TZ="Asia/Tokyo"
LANG=ja_JP.UTF-8

pushd ./%{gem_instdir}
# Some files are missing and due to it some tests fail, skip
# also some tests fail because the order of the xml output in test_document
# can be swapped.
SKIPTEST="test/xml/test_xinclude.rb test/xml/test_document.rb"
for f in $SKIPTEST
do
	mv $f $f.skip
done

%{?scl:scl enable %scl - << \EOF}
ruby -I.:lib:test -e \
	"require 'minitest/autorun' ; Dir.glob('test/**/test_*.rb'){|f| require f}"
%{?scl:EOF}

for f in $SKIPTEST
do
	mv $f.skip $f
done

popd

%files
%defattr(-,root, root,-)
%{_bindir}/%{gem_name}
%{gem_extdir}/
%dir	%{gem_instdir}/
%doc	%{gem_instdir}/[A-Z]*
%doc	%{gem_instdir}/nokogiri_help_responses.md
%exclude %{gem_instdir}/Rakefile
%{gem_instdir}/bin/
%{gem_instdir}/lib/
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%if 0
%files	jruby
%defattr(-,root,root,-)
%{gem_instdir}/ext/java/
%endif

%files	doc
%defattr(-,root,root,-)
%{gem_instdir}/Rakefile
#%%{gem_instdir}/deps.rip
#%%{gem_instdir}/spec/
%{gem_instdir}/tasks/
%{gem_instdir}/test/
%{gem_dir}/doc/%{gem_name}-%{version}/

%changelog
* Sat Sep 29 2012 Troy Dawson <tdawson@redhat.com> - 1.5.2-4
- Release bump for rebuild into both i386 and x86_64

* Tue Jul 10 2012 Troy Dawson <tdawson@redhat.com> - 1.5.2-3
- Fixed and overzelous find and replace

* Mon Jul 09 2012 Troy Dawson <tdawson@redhat.com> - 1.5.2-2
- Changed spec file to work with scl
- Changed spec file to work with scl, rh7+, and fedora17+ only

* Mon Apr  9 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.2-1
- 1.5.2

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.5.0-3
- Fix conditionals for F17 to work for RHEL 7 as well.

* Tue Jan 24 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.0-2
- F-17: rebuild for ruby19
- For now aviod build failure by touching some files

* Thu Jan 18 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.0-1
- 1.5.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.5.beta4.1
- F-17: Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.0-0.5.beta4
- Remove unneeded patch

* Thu Mar 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.0-0.4.beta4
- Patch for newer rake to make testsuite run

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.3.beta4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0-0.3.beta4
- 1.5.0.beta.4

* Tue Dec  7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0-0.2.beta3
- 1.5.0.beta.3

* Sun Oct 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0-0.1.beta2
- Try 1.5.0.beta.2

* Fri Jul 30 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.3.1-1
- 1.4.3.1

* Wed May 26 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.2-1
- 1.4.2

* Thu Apr 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.1-2
- Fix build failure with libxml2 >= 2.7.7

* Tue Dec 15 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.1-1
- 1.4.1

* Mon Nov  9 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.0-1
- 1.4.0

* Sat Aug 22 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.3-2
- Fix test failure on sparc

* Wed Jul 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.3-1
- 1.3.3

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.2-3
- F-12: Mass rebuild

* Thu Jul  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.2-2
- Enable test
- Recompile with -O2

* Thu Jun 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.2-1
- 1.3.2

* Thu Jun 11 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.1-1
- 1.3.1

* Thu Mar 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.3-1
- 1.2.3

* Thu Mar 19 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.2-1
- 1.2.2

* Thu Mar 12 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.1-1
- 1.2.1

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.1-2
- F-11: Mass rebuild

* Thu Jan 15 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.1-1
- 1.1.1

* Thu Dec 25 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.0-1
- Initial packaging

