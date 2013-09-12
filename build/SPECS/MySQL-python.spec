%{?scl:%scl_package MySQL-python}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}MySQL-python
Version:        1.2.3
Release:        1%{?dist}
Summary:        MySQL database adapter for Python

Group:          Development/Languages
License:        MIT
URL:            http://sourceforge.net/projects/mysql-python/
Source0:	http://hivelocity.dl.sourceforge.net/project/mysql-python/mysql-python/1.2.3/MySQL-python-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      x86_64
BuildRequires:  %{?scl_prefix}python-devel
Requires:       %{?scl_prefix}python-setuptools
Requires:       %{?scl_prefix}python-devel

%description
MySQLdb is a Python DB API-2.0-compliant interface; see PEP-249 for details. For up-to-date versions of MySQLdb, use the homepage link.

Supported versions:

* MySQL versions from 3.23 to 5.5; 5.0 or newer recommended. MariaDB should also work.
* Python versions 2.4-2.7; Python 3 support coming soon.

%prep
%setup -q -n MySQL-python-%{version}

%build
# Build code
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%install
rm -rf $RPM_BUILD_ROOT
%{?scl:scl enable %{scl} "}
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
%{?scl:"}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc doc/FAQ.txt doc/MySQLdb.txt README HISTORY
%{python_sitearch}/*

%changelog
* Wed Aug 21 2013 Baron Chandler <baron.chandler@wisertogether.com> 1.2.3-1
  Built for SCL/OpenShift
