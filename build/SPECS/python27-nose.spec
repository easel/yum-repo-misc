%{?scl:%scl_package python-nose}
%{!?scl:%global pkg_name %{name}}

%global upstream_name nose

# Enable building without docs to avoid a circular dependency between this and python-sphinx
%global with_docs 0

Name:           %{?scl_prefix}python-nose
Version:        1.2.1
Release:        6%{?dist}
Summary:        Discovery-based unittest extension for Python

Group:          Development/Languages
License:        LGPLv2+ and Public Domain
URL:            http://somethingaboutorange.com/mrl/projects/nose/
Source0:        http://pypi.python.org/packages/source/n/nose/nose-%{version}.tar.gz
# Submitted upstream: http://code.google.com/p/python-nose/issues/detail?id=421
Patch1: nose-manpage.patch
Patch2: nose-make-test_multiprocessing-reliable.patch

BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python2-devel
BuildRequires:  %{?scl_prefix}python-setuptools
BuildRequires:  dos2unix
BuildRequires:  %{?scl_prefix}python-coverage >= 3.4-1
Requires:       %{?scl_prefix}python-setuptools

%description
nose extends the test loading and running features of unittest, making
it easier to write, find and run tests.

By default, nose will run tests in files or directories under the
current working directory whose names include "test" or "Test" at a
word boundary (like "test_this" or "functional_test" or "TestClass"
but not "libtest"). Test output is similar to that of unittest, but
also includes captured stdout output from failing tests, for easy
print-style debugging.

These features, and many more, are customizable through the use of
plugins. Plugins included with nose provide support for doctest, code
coverage and profiling, flexible attribute-based test selection,
output capture and more.

%package docs
Summary:        Nose Documentation
Group:          Documentation
%if 0%{?with_docs}
BuildRequires:  %{?scl_prefix}python-sphinx
%endif
Requires:       %{?scl_prefix}python-nose

%description docs
Documentation for Nose

%prep
%setup -q -n %{upstream_name}-%{version}
%patch1 -p1 -b .manp
%patch2 -p1

dos2unix examples/attrib_plugin.py

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%install
rm -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install --skip-build --root %{buildroot} \
           --install-data=%{_datadir}
%{?scl:"}

%if 0%{?with_docs}
pushd doc
%{?scl:scl enable %{scl} "}
make html
%{?scl:"}
rm -rf .build/html/.buildinfo .build/html/_sources
mv .build/html ..
rm -rf .build
popd
%endif # with_docs
cp -a doc reST
rm -rf reST/.static reST/.templates


%check
%{?scl:scl enable %{scl} "}
%{__python} selftest.py
%{?scl:"}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG lgpl.txt NEWS README.txt
%{_bindir}/nosetests
%{_bindir}/nosetests-%{python_version}
%{_mandir}/man1/nosetests.1.gz
%{python_sitelib}/nose*

%files docs
%defattr(-,root,root,-)
%doc reST examples
%if 0%{?with_docs}
%doc html
%endif # with_docs

%changelog
* Fri Jun 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.1-6
- Fix the race condition in some multiprocessing tests. Fixes rhbz#967222.

* Tue May 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.1-5
- Rebuild to generate bytecode properly after fixing rhbz#956289
- scl-utils now compile man-pages -> use proper name in %%files.

* Wed Oct 10 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.1-4
- Enable building with documentation, now really.

* Wed Sep 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.1-3
- Enable building with documentation.

* Wed Sep 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.1-2
- Rebuilt for SCL.

* Wed Sep 12 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.1-1
- New upsream 1.2.1 that just bumps the version properly

* Mon Sep 10 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.0-1
- Update to nose-1.2.0.
- Two less python3 test failures than 1.1.2

* Sat Aug  4 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.2-5
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3
- disable selftests that fail under 3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.2-4
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 1 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1.2-1
- Upstream bugfix release

* Wed Jul 27 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1.1-1
- Upstream bugfix release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 26 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- Create the docs subpackage for text docs even if we don't create the html docs.
- Make python3 subpackage

* Tue Dec 7 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.11.4-2
- Fix FTBFS with newer coverage

* Thu Oct 21 2010 Luke Macken <lmacken@redhat.com> - 0.11.4-1
- Update to 0.11.4 (#3630722)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.11.3-5
- add support for building without docs, to avoid a circular build-time
dependency between this and python-sphinx; disable docs subpackage for now
- add (apparently) missing BR on python-coverage (appears to be needed
for %%check)
- cherrypick upstream compatibility fixes for 2.7

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu May 20 2010 Luke Macken <lmacken@redhat.com> - 0.11.3-3
- Update URL to http://code.google.com/p/python-nose/
- Align description to reflect that in setup.py
- Create a docs subpackage containing HTML & reST documentation
- Thanks to Gareth Armstrong at HP for the patch

* Thu May 06 2010 Luke Macken <lmacken@redhat.com> - 0.11.3-2
- Don't hardcode the python version

* Thu May 06 2010 Luke Macken <lmacken@redhat.com> - 0.11.3-1
- Update to 0.11.3
- Enable the self tests

* Mon Oct 05 2009 Luke Macken <lmacken@redhat.com> - 0.11.1-2
- Include the new nosetests-2.6 script as well

* Mon Oct 05 2009 Luke Macken <lmacken@redhat.com> - 0.11.1-1
- Update to 0.11.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.10.4-1
- Update to 0.10.4 to fix 2.6 issues

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.10.3-2
- Rebuild for Python 2.6

* Sat Aug 02 2008 Luke Macken <lmacken@redhat.com> 0.10.3-1
- Update to 0.10.3

* Thu Feb 28 2008 Luke Macken <lmacken@redhat.com> 0.10.1-1
- Update to 0.10.1

* Mon Dec  3 2007 Luke Macken <lmacken@redhat.com> 0.10.0-2
- Add python-setuptools to Requires (Bug #408491)

* Tue Nov 27 2007 Luke Macken <lmacken@redhat.com> 0.10.0-1
- 0.10.0

* Sun Sep  2 2007 Luke Macken <lmacken@redhat.com> 0.10.0-0.3.b1
- Update for python-setuptools changes in rawhide

* Tue Aug 21 2007 Luke Macken <lmacken@redhat.com> 0.10.0-0.2.b1
- 0.10.0b1
- Update license tag to LGPLv2

* Fri Jun 20 2007 Luke Macken <lmacken@redhat.com> 0.10.0-0.1.a2
- 0.10.0a2

* Sat Jun  2 2007 Luke Macken <lmacken@redhat.com> 0.9.3-1
- Latest upstream release
- Remove python-nose-0.9.2-mandir.patch

* Sat Mar  3 2007 Luke Macken <lmacken@redhat.com> 0.9.2-1
- Add nosetests(1) manpage, and python-nose-0.9.2-mandir.patch to put it in
  the correct location.
- 0.9.2

* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> 0.9.1-2
- Rebuild for python 2.5

* Fri Nov 24 2006 Luke Macken <lmacken@redhat.com> 0.9.1-1
- 0.9.1

* Fri Sep  8 2006 Luke Macken <lmacken@redhat.com> 0.9.0-1
- 0.9.0

* Wed Apr 19 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.7.2-1
- Initial RPM release
