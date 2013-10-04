%{?scl:%scl_package python-pip}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}python-pip
Version:        1.4.1
Release:        1%{?dist}
Summary:        A tool for installing and managing Python packages

Group:          Development/Libraries
License:        MIT
URL:            http://www.pip-installer.org
Source0:        http://pypi.python.org/packages/source/p/pip/pip-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires:       %{?scl_prefix}python-setuptools

%description
Pip is a replacement for `easy_install
<http://peak.telecommunity.com/DevCenter/EasyInstall>`_.  It uses mostly the
same techniques for finding packages, so packages that were made
easy_installable should be pip-installable as well.

%package virtualenv
Summary:        Python Virtual Environment cache for pip
Group:		Development/Libraries

Requires:       %{?scl_prefix}python-virtualenv

%description virtualenv

Installs the pip source tarfile for installation into new virtual
environments.

%prep
%setup -q -n pip-%{version}

%{__sed} -i '1d' pip/__init__.py


%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py sdist
%{?scl:"}

%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}


%install
%{__rm} -rf %{buildroot}

%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}

install -D -m 644 dist/pip-%{version}.tar.gz %{buildroot}/%{python_sitelib}/virtualenv_support/pip-%{version}.tar.gz

pushd %{buildroot}%{_bindir}
# The install process creates both pip and pip-<python_abiversion> that seem to
# be the same. Since removing pip-* also clobbers pip-python3, just remove pip-2*
%{__rm} -rf pip-2*

# The pip executable no longer needs to be renamed to avoid conflict with perl-pip
# https://bugzilla.redhat.com/show_bug.cgi?id=958377
# However, we'll keep a python-pip alias for now
ln -s pip python-pip

# after changing the pip-python binary name, make a symlink to the old name,
# that will be removed in a later version
# https://bugzilla.redhat.com/show_bug.cgi?id=855495
ln -s pip pip-python
popd


%clean
%{__rm} -rf %{buildroot}

# unfortunately, pip's test suite requires virtualenv >= 1.6 which isn't in
# fedora yet. Once it is, check can be implemented

%files
%defattr(-,root,root,-)
%doc PKG-INFO docs
%attr(755,root,root) %{_bindir}/pip
%attr(755,root,root) %{_bindir}/pip-python
%attr(755,root,root) %{_bindir}/python-pip
%{python_sitelib}/pip*

%files virtualenv
%attr(644,root,root) %{python_sitelib}/virtualenv_support/pip-%{version}.tar.gz

%changelog
* Tue Aug  6 2013 Robert Millner <rmillner@redhat.com> - 1.4-6
- Add virtualenv package with source rebuilt after applying patches.

* Tue Aug  6 2013 Robert Millner <rmillner@redhat.com> - 1.4-5
- Configure for Python SCL environment.
- Remove python3 build since SCL deals with python3 in a different way.
- Use version 1.4 of pip and verify patch we supplied with 1.3.1 is included.

* Tue Jul 16 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.1-4
- Fix for CVE 2013-2099

* Thu May 23 2013 Tim Flink <tflink@fedoraproject.org> - 1.3.1-3
- undo python2 executable rename to python-pip. fixes #958377
- fix summary to match upstream

* Mon May 06 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.3.1-2
- Fix main package Summary, it's for Python 2, not 3 (#877401)

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.1-1
- Update to 1.3.1, fix for CVE-2013-1888.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 Tim Flink <tflink@fedoraproject.org> - 1.2.1-2
- Fixing files for python3-pip

* Thu Oct 04 2012 Tim Flink <tflink@fedoraproject.org> - 1.2.1-1
- Update to upstream 1.2.1
- Change binary from pip-python to python-pip (RHBZ#855495)
- Add alias from python-pip to pip-python, to be removed at a later date

* Tue May 15 2012 Tim Flink <tflink@fedoraproject.org> - 1.1.0-1
- Update to upstream 1.1.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 22 2011 Tim Flink <tflink@fedoraproject.org> - 1.0.2-1
- update to 1.0.2 and added python3 subpackage

* Wed Jun 22 2011 Tim Flink <tflink@fedoraproject.org> - 0.8.3-1
- update to 0.8.3 and project home page

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Luke Macken <lmacken@redhat.com> - 0.8.2-1
- update to 0.8.2 of pip
* Mon Aug 30 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.8-1
- update to 0.8 of pip
* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 7 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.7.2-1
- update to 0.7.2 of pip
* Sun May 23 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.7.1-1
- update to 0.7.1 of pip
* Fri Jan 1 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1.4
- fix dependency issue
* Tue Dec 18 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1-2
- fix spec file 
* Mon Dec 17 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1-1
- upgrade to 0.6.1 of pip
* Mon Aug 31 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.4-1
- Initial package



