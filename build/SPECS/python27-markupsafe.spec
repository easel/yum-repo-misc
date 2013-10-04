%{?scl:%scl_package python-markupsafe}
%{!?scl:%global pkg_name %{name}}

Name: %{?scl_prefix}python-markupsafe
Version: 0.11
Release: 11%{?dist}
Summary: Implements a XML/HTML/XHTML Markup safe string for Python

Group: Development/Languages
License: BSD
URL: http://pypi.python.org/pypi/MarkupSafe
Source0: http://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: %{?scl_prefix}python-devel
BuildRequires: %{?scl_prefix}python-setuptools

%description
A library for safe markup escaping.

%prep
%setup -q -n MarkupSafe-%{version}

%build
%{?scl:scl enable %{scl} - << \EOF}
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
%{?scl:EOF}

%install
rm -rf $RPM_BUILD_ROOT
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{?scl:"}
# C code errantly gets installed
rm $RPM_BUILD_ROOT/%{python_sitearch}/markupsafe/*.c

%check
%{?scl:scl enable %{scl} "}
%{__python} setup.py test
%{?scl:"}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README.rst
%{python_sitearch}/*

%changelog
* Tue May 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.11-11
- Rebuild to generate bytecode properly after fixing rhbz#956289

* Mon Dec 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.11-10
- Bump again to build properly on ppc64

* Mon Dec 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.11-9
- Rebuilt for PPC.

* Wed Sep 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.11-8
- Rebuilt for SCL.

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.11-7
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 0.11-6
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 David Malcolm <dmalcolm@redhat.com> - 0.11-2
- rebuild for newer python3

* Thu Sep 30 2010 Luke Macken <lmacken@redhat.com> - 0.11-1
- Update to 0.11

* Wed Aug 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.9.2-5
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Fri Jul 23 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 24 2010 Kyle VanderBeek <kylev@kylev.com> - 0.9.2-3
- Fix missing setuptools BuildRequires.

* Thu Jun 24 2010 Kyle VanderBeek <kylev@kylev.com> - 0.9.2-2
- Fixed sitearch and python3 definitions to work better with older Fedora/RHEL.

* Wed Jun 23 2010 Kyle VanderBeek <kylev@kylev.com> - 0.9.2-1
- Initial version.
