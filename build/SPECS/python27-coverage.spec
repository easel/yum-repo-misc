%{?scl:%scl_package python-coverage}
%{!?scl:%global pkg_name %{name}}

%global _use_internal_dependency_generator 0
%global __find_provides /bin/sh -c "%{_rpmconfigdir}/find-provides | grep -v -E '(tracer.so)' || /bin/true"
%global __find_requires /bin/sh -c "%{_rpmconfigdir}/find-requires | grep -v -E '(tracer.so)' || /bin/true"

Name:           %{?scl_prefix}python-coverage
Summary:        Code coverage testing module for Python
Version:        3.5.3
Release:        2%{?dist}
License:        BSD and (MIT or GPLv2)
Group:          System Environment/Libraries
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:            http://nedbatchelder.com/code/modules/coverage.html
Source0:        http://pypi.python.org/packages/source/c/coverage/coverage-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}python-setuptools, %{?scl_prefix}python-devel
Requires:       %{?scl_prefix}python-setuptools

%description
Coverage.py is a Python module that measures code coverage during Python 
execution. It uses the code analysis tools and tracing hooks provided in the 
Python standard library to determine which lines are executable, and which 
have been executed.

%prep
%setup -q -n coverage-%{version}

find . -type f -exec chmod 0644 \{\} \;
sed -i 's/\r//g' README.txt

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%install
rm -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}

%clean
rm -rf %{buildroot}

%files
%doc README.txt
%{_bindir}/coverage
%{python_sitearch}/coverage/
%{python_sitearch}/coverage*.egg-info/

%changelog
* Tue May 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 3.5.3-2
- Rebuild to generate bytecode properly after fixing rhbz#956289

* Mon Dec 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.5.3-1
- Rebuilt for PPC.
- Updated to version 3.5.3.

* Wed Oct 17 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.5.2-0.6.b1
- Rebuilt for RHEL 5.

* Wed Sep 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.5.2-0.5.b1
- Rebuilt for SCL.

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 3.5.2-0.4.b1
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 3.5.2-0.3.b1
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.2-0.2.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  2 2012 Tom Callaway <spot@fedoraproject.org> - 3.5.2-0.1.b1
- update to 3.5.2b1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-0.2.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep  2 2011 Tom Callaway <spot@fedoraproject.org> - 3.5.1-0.1.b1
- update to 3.5.1b1

* Mon Jun  6 2011 Tom Callaway <spot@fedoraproject.org> - 3.5-0.1.b1
- update to 3.5b1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010  <David Malcolm <dmalcolm@redhat.com>> - 3.4-2
- rebuild for newer python3

* Thu Oct 21 2010 Luke Macken <lmacken@redhat.com> - 3.4-1
- Update to 3.4 (#631751)

* Fri Sep 03 2010 Luke Macken <lmacken@redhat.com> - 3.3.1-4
- Rebuild against Python 3.2

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed May 9 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 3.3.1-2
- Fix license tag, permissions, and filtering extraneous provides

* Wed May 9 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1

* Fri Feb  5 2010 David Malcolm <dmalcolm@redhat.com> - 3.2-3
- add python 3 subpackage (#536948)

* Sun Jan 17 2010 Luke Macken <lmacken@redhat.com> - 3.2-2
- Require python-setuptools (#556290)

* Wed Dec  9 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2-1
- update to 3.2

* Fri Oct 16 2009 Luke Macken <lmacken@redhat.com> - 3.1-1
- Update to 3.1

* Wed Aug 10 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.0.1-1
- update to 3.0.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 15 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.85-2
- fix install invocation

* Wed May 6 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.85-1
- Initial package for Fedora
