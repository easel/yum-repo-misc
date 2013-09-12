%{?scl:%scl_package python-psycopg2}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}python-psycopg2
Version:        2.5.1
Release:        1%{?dist}
Summary:        PostgreSQL database adapter for Python

Group:          Development/Languages
License:        MIT
URL:            http://pypi.python.org/pypi/psycopg2
Source0:        http://pypi.python.org/packages/source/p/psycopg2/psycopg2-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      x86_64
BuildRequires:  %{?scl_prefix}python-devel
Requires:       %{?scl_prefix}python-setuptools
Requires:       %{?scl_prefix}python-devel
Requires:	postgresql92-postgresql-devel

%description
psycopg2 is a PostgreSQL database adapter for the Python programming language.
psycopg2 was written with the aim of being very small and fast, and stable as a
rock.

psycopg2 is different from the other database adapter because it was designed
for heavily multi-threaded applications that create and destroy lots of cursors
and make a conspicuous number of concurrent INSERTs or UPDATEs. psycopg2 also
provide full asynchronous operations and support for coroutine libraries.

%prep
%setup -q -n psycopg2-%{version}

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
%doc doc/COPYING doc/COPYING.LESSER doc/HACKING doc/pep-0249.txt doc/psycopg2.txt doc/README doc/SUCCESS
%{python_sitearch}/*

%changelog
* Fri Aug 15 2013 Baron Chandler <baron.chandler@wisertogether.com> 2.5.1-1
  Built for SCL/OpenShift
