%{?scl:%scl_package python-pygments}
%{!?scl:%global pkg_name %{name}}

%global upstream_name Pygments

Name:           %{?scl_prefix}python-pygments
Version:        1.5
Release:        2%{?dist}
Summary:        Syntax highlighting engine written in Python

Group:          Development/Libraries
License:        BSD
URL:            http://pygments.org/
Source0:        http://pypi.python.org/packages/source/P/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python2-devel >= 2.4, %{?scl_prefix}python-setuptools, %{?scl_prefix}python-nose
Requires:       %{?scl_prefix}python-setuptools

%description
Pygments is a generic syntax highlighter for general use in all kinds
of software such as forum systems, wikis or other applications that
need to prettify source code. Highlights are:

  * a wide range of common languages and markup formats is supported
  * special attention is paid to details that increase highlighting
    quality
  * support for new languages and formats are added easily; most
    languages use a simple regex-based lexing mechanism
  * a number of output formats is available, among them HTML, RTF,
    LaTeX and ANSI sequences
  * it is usable as a command-line tool and as a library
  * ... and it highlights even Brainf*ck!


%prep
%setup -q -n Pygments-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}
%{__sed} -i 's/\r//' LICENSE

%install
rm -rf $RPM_BUILD_ROOT

%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{?scl:"}

pushd docs
install -d %{buildroot}%{_mandir}/man1
mv pygmentize.1 $RPM_BUILD_ROOT%{_mandir}/man1/pygmentize.1
mv build html
mv src reST
popd

%clean
rm -rf $RPM_BUILD_ROOT

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGES docs/html docs/reST LICENSE TODO
%{python_sitelib}/*
%{_bindir}/pygmentize
%lang(en) %{_mandir}/man1/pygmentize.1.gz

%changelog
* Tue May 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.5-2
- Rebuild to generate bytecode properly after fixing rhbz#956289

* Thu Jan 31 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.5-1
- Updated to version 1.5.

* Wed Sep 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4-8
- Rebuilt for SCL.
- python-imaging is only a soft dependency, removing it for now.

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.4-7
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 1.4-6
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 13 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.4-3
- Really enable the python3 unittests.
- Fix python26 byte compilation (thanks to Jeffrey Ness)

* Sat Sep 10 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.4-2
- Fix python main package having dependencies for the python2.6 subpackage
- Fix places that used the default python instead of python26
- Attempt to make byte compilation more robust in case we add python3 to EPEL5
- Run unittests on python3 in F15+

* Fri Jun 24 2011 Steve Milner <smilner@fedoraproject.org> - 1.4-1
- update for upstream release
- Add python2.6 support done by Steve Traylen <steve.traylen@cern.ch>. BZ#662755.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.3.1-7
- update to most recent python guidelines
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu May  6 2010 Gareth Armstrong <gareth.armstrong@hp.com> - 1.3.1-5
- Enforce that Pygments requires Python 2.4 or later via an explicit BR
- Minor tweaks to spec file
- Deliver html and reST doc files to specifically named directories
- Align description with that of http://pygments.org/
- Add %%check section for Python2 and add BR on python-nose

* Fri Apr 23 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.3.1-4
- switched with_python3 back to 1

* Fri Apr 23 2010 David Malcolm <dmalcolm@redhat.com> - 1.3.1-3
- add python3 subpackage (BZ#537244), ignoring soft-dep on imaging for now

* Sat Apr 13 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.3.1-2
- added python-imaging as a dependency per BZ#581663.

* Sat Mar  6 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.3.1-1
- Updated for release.

* Tue Sep 29 2009 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.1.1-1
- Updated for release.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.0-3
- Updated for release.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0-2
- Rebuild for Python 2.6

* Fri Nov 27 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.0-1
- Updated for upstream 1.0.

* Sun Sep 14 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 0.11.1-1
- Updated for upstream 0.11.

* Mon Jul 21 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 0.10-1
- Updated for upstream 0.10.

* Thu Nov 29 2007 Steve 'Ashcrow' Milner <me@stevemilner.org> - 0.9-2
- Added python-setuptools as a Requires per bz#403601.

* Mon Nov 12 2007 Steve 'Ashcrow' Milner <me@stevemilner.org> - 0.9-1
- Updated for upstream 0.9.

* Thu Aug 17 2007 Steve 'Ashcrow' Milner <me@stevemilner.org> - 0.8.1-2
- Removed the dos2unix build dependency.

* Thu Jun 28 2007 Steve 'Ashcrow' Milner <me@stevemilner.org> - 0.8.1-1
- Initial packaging for Fedora.
