%{?scl:%scl_package nodejs-ansi}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}


Name:       %{?scl_prefix}nodejs-ansi
Version:    0.1.2
Release:    7%{?dist}
Summary:    ANSI escape codes for Node.js
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/TooTallNate/ansi.js
# the source contains a nonfree image file, which is removed by the Source1 script
Source0:    ansi-%{version}-stripped.tgz
Source1:    nodejs-ansi-tarball.sh
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
ansi.js is a module for Node.js that provides an easy-to-use API for writing
ANSI escape codes to Stream instances. ANSI escape codes are used to do fancy
things in a terminal window, like render text in colors, delete characters,
lines, the entire window, or hide and show the cursor, and lots more!

%prep
%setup -q -n package

#fix perms in stuff that goes in %%doc
chmod 0644 examples/*.js examples/*/*

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/ansi
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/ansi

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/ansi
%doc README.md examples

%changelog
* Fri May 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-7
- remove nonfree image

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-6
- add macro for EPEL6 dependency generation

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.2-6
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-4
- fix permissions correctly

* Fri Jan 11 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-3
- fix permissions in example

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-2
- add missing build section
- fix incorrect summary

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-1
- New upstream release 0.1.2

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.0-1
- new upstream release 0.1.0

* Fri Mar 16 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-1
- initial package
