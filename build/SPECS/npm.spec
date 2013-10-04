%{?scl:%scl_package npm}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}npm
Version:    1.2.17
Release:    9%{?dist}
Summary:    Node.js Package Manager
License:    MITNFA
Group:      Development/Tools
URL:        http://npmjs.org/
Source0:    npm-1.2.17-stripped.tar.gz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires: %{?scl_prefix}nodejs-devel
# revert a change that adds a dep (that only affects Windows anyway)
Patch1:     npm-revert-cmd-shim.patch
Patch2:	    add-.gz-file-extension-when-npm-call-man-fix-manpath.patch
Patch3:	    RHBZ-983930-CVE-2013-4116-Insecure-temporary-directo.patch
%{?scl:Requires: %{scl}-runtime}

%description
npm is a package manager for node.js. You can use it to install and publish your
node programs. It manages dependencies and does other cool stuff.

%prep
%setup -q -n package
%patch1 -p1
%patch2 -p1
%patch3 -p1
%nodejs_fixdep lru-cache 2.3.x
%nodejs_fixdep init-package-json 0.0.x
%nodejs_fixdep read-package-json 0.3.x

#remove bundled modules
rm -rf node_modules

#add a missing shebang
sed -i -e '1i#!/usr/bin/env node' bin/read-package-json.js

# prefix all manpages with "npm-"
pushd man
for dir in *; do
    pushd $dir
    for page in *; do
        if [[ $page != npm* ]]; then
            mv $page npm-$page
        fi
    done
    popd
done
popd

# delete windows stuff
rm bin/npm.cmd bin/node-gyp-bin/node-gyp.cmd

# globals.1 and folders.1 are the same package and the former is outdated
# https://github.com/isaacs/npm/issues/3078
ln -sf npm-folders.1 man/man1/npm-global.1

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/npm
cp -pr bin lib cli.js package.json %{buildroot}%{nodejs_sitelib}/npm/

mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/npm/bin/npm-cli.js %{buildroot}%{_bindir}/npm

# ghosted global config files
mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/npmrc
touch %{buildroot}%{_sysconfdir}/npmignore

# install to mandir with "npm-" prefix, but create symlinks without it
# otherwise npm help doesn't work
mkdir -p %{buildroot}%{_mandir}
mkdir -p %{buildroot}%{nodejs_sitelib}/npm/man
cp -pr man/* %{buildroot}%{_mandir}/
for section in `ls -1 %{buildroot}%{_mandir}`;do
    pushd "%{buildroot}%{_mandir}/${section}"
    mkdir -p "%{buildroot}%{nodejs_sitelib}/npm/man/${section}"
    for page in *;do
        ln -sf "%{_mandir}/${section}/${page}.gz" \
               "%{buildroot}%{nodejs_sitelib}/npm/man/${section}/${page/npm-/}"
    done
    popd
done

#ln -sf %{_defaultdocdir}/%{name}-%{version} %{buildroot}%{nodejs_sitelib}/npm/doc

%nodejs_symlink_deps

# probably needs network, need to investigate further
#%%check
#%%__nodejs test/run.js
#%%tap test/tap/*.js

%clean
rm -rf %{buildroot}

%pretrans
# workaround for rpm bug 646523, can be removed in F21
[ $1 -eq 0 ] && [ -L %{nodejs_sitelib}/npm/man ] && \
rm -f %{nodejs_sitelib}/npm/man || :


%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/npm
%ghost %{_sysconfdir}/npmrc
%ghost %{_sysconfdir}/npmignore
%{_bindir}/npm
%{_mandir}/man1/*
%{_mandir}/man3/*
%doc AUTHORS doc/* html README.md LICENSE

%changelog
* Mon Jul 22 2013 Tomas Hrcka thrcka@redhat.com - 1.2.17-9
- RHBZ #983930 CVE-2013-4116 Insecure temporary directory generation 

* Mon Jul 22 2013 Tomas Hrcka  <thrcka@redhat.com> - 1.2.17-8
- patch for font deletion was replaced by script that strip webfons from tarball

* Tue Jul 18 2013 Tomas Hrcka  <thrcka@redhat.com> - 1.2.17-7
- Removed badly licensed fonts from html documentation

* Tue Jul 02 2013 Tomas Hrcka  <thrcka@redhat.com> - 1.2.17-6
- replaced manpath to use system paths
- replaced previous patch to fix gz extension

* Sun Jun 02 2013 Tomas Hrcka <thrcka@redhat.com> - 1.2.17-5.2
- patch that add .gz extension when help.js calls 'man' fix RHBZ#965439 

* Tue May 07 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.17-5.1
- Add runtime dependency on scl-runtime

* Wed Apr 17 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.17-5
- Fix manpage names so that npm help finds them

* Mon Apr 15 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.17-4.1
- Fix documentation symlink
- Use new requires/provides macro

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.17-4
- add EPEL dependency generation macro

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.17-3
- rebuilt

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.17-2
- revert a change that adds a dep (that only affects Windows anyway)
- fix bogus date in changelog warning

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.17-2
- Add support for software collections

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.17-1
- new upstream release 1.2.17

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.14-2
- fix dependencies

* Mon Mar 11 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.2.14-1
- New upstream release 1.2.14
- Bring npm up to the latest to match the Node.js 0.10.0 release

* Wed Feb 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.10-2
- fix dep for updated read-package-json

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.10-1
- new upstream release 1.2.10

* Sat Jan 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.1-2
- fix rpmlint warnings

* Fri Jan 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.1-1
- new upstream release 1.2.1
- fix License tag

* Thu Jan 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.0-1
- new upstream release 1.2.0

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.70-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.70-1
- new upstream release 1.1.70

* Wed May 02 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.19-1
- New upstream release 1.1.19

* Wed Apr 18 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.18-1
- New upstream release 1.1.18

* Fri Apr 06 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.16-1
- New upstream release 1.1.16

* Mon Apr 02 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.15-1
- New upstream release 1.1.15

* Thu Mar 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.14-1
- New upstream release 1.1.14

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.13-2
- new dependencies fstream-npm, uid-number, and fstream-ignore (indirectly)

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.13-1
- new upstream release 1.1.13

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.12-1
- new upstream release 1.1.12

* Thu Mar 15 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.9-1
- new upstream release 1.1.9

* Sun Mar 04 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-1
- new upstream release 1.1.4

* Sat Feb 25 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.2-1
- new upstream release 1.1.2

* Sat Feb 11 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-2
- fix node_modules symlink

* Thu Feb 09 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-1
- new upstream release 1.1.1

* Sun Jan 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-2.3
- new upstream release 1.1.0-3

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-2.2
- missing Group field for EL5

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-1.2
- new upstream release 1.1.0-2

* Thu Nov 17 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.106-1
- new upstream release 1.0.106
- ship manpages again

* Thu Nov 10 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.105-1
- new upstream release 1.0.105
- use relative symlinks instead of absolute
- fixes /usr/bin/npm symlink on i686

* Mon Nov 07 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.104-1
- new upstream release 1.0.104
- adds node 0.6 support

* Wed Oct 26 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.101-2
- missing Requires on nodejs-request
- Require compilers too so native modules build properly

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.101-1
- new upstream release
- use symlink /usr/lib/node_modules -> /usr/lib/nodejs instead of patching

* Thu Aug 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.26-2
- rebuilt with fixed nodejs_fixshebang macro from nodejs-devel-0.4.11-3

* Tue Aug 23 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.26-1
- initial package
