%{?scl:%scl_package python-werkzeug}
%{!?scl:%global pkg_name %{name}}

%global srcname Werkzeug

Name:           %{?scl_prefix}python-werkzeug
Version:        0.8.3
Release:        5%{?dist}
Summary:        The Swiss Army knife of Python web development 

Group:          Development/Libraries
License:        BSD
URL:            http://werkzeug.pocoo.org/
Source0:        http://pypi.python.org/packages/source/W/Werkzeug/%{srcname}-%{version}.tar.gz
Patch1:		werkzeug-fips-errors-fix.patch
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
BuildRequires:  %{?scl_prefix}python-sphinx

%description
Werkzeug
========

Werkzeug started as simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules.  It includes a powerful debugger, full featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

Werkzeug is unicode aware and doesn't enforce a specific template
engine, database adapter or anything else.  It doesn't even enforce
a specific way of handling requests and leaves all that up to the
developer. It's most useful for end user applications which should work
on as many server environments as possible (such as blogs, wikis,
bulletin boards, etc.).

%package doc
Summary:        Documentation for %{pkg_name}
Group:          Documentation
Requires:       %{?scl_prefix}%{pkg_name} = %{version}-%{release}


%description doc
Documentation and examples for %{pkg_name}.

%prep
%setup -q -n %{srcname}-%{version}
%{__sed} -i 's/\r//' LICENSE
%{__sed} -i '1d' werkzeug/testsuite/multipart/collect.py
%patch1 -p1


%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}
find examples/ -name '*.py' -executable | xargs chmod -x
find examples/ -name '*.png' -executable | xargs chmod -x
pushd docs
%{?scl:scl enable %{scl} "}
make html
%{?scl:"}
popd

%install
%{__rm} -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}
%{__rm} -rf docs/_build/html/.buildinfo
%{__rm} -rf examples/cupoftee/db.pyc

%check
%{?scl:scl enable %{scl} "}
%{__python} setup.py test
%{?scl:"}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE PKG-INFO CHANGES
%{python_sitelib}/*

%files doc
%defattr(-,root,root,-)
%doc docs/_build/html examples

%changelog
* Wed May 15 2013 Matej Stuchlik <mstuchli@redhat.com> - 0.8.3-5
- Improved error messages in FIPS

* Tue May 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.3-4
- Rebuild to generate bytecode properly after fixing rhbz#956289

* Wed Sep 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.3-3
- Rebuilt for SCL.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb  5 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 0.8.3-1
- upstream 0.8.3 (fixes XSS security issues)

* Wed Jan 25 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 0.8.2-1
- upstream 0.8.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun May 23 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.2-1
- Updating because upstream release of Werkzeug 0.6.2
* Sat Mar 05 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6-1
- Updating because upstream release of Werkzeug 0.6
* Tue Aug 25 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.5.1-1
- Initial package
