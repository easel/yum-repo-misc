Summary: PhantomJS is a headless WebKit with JavaScript API
Name: phantomjs
Version: 1.8.1
Release: 1%{?dist}
License: BSD
Group: unknown
URL: http://code.google.com/p/phantomjs/
Source0: %{name}-%{version}-source.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: openssl-devel >= 0.9.7, freetype-devel, fontconfig-devel

%description
PhantomJS is a headless WebKit with JavaScript API. It has fast
and native support for various web standards: DOM handling,
CSS selector, JSON, Canvas, and SVG.
PhantomJS is created by Ariya Hidayat.

%prep
%setup -q

%build
./build.sh --confirm --jobs "`grep "^processor" /proc/cpuinfo | wc -l`"
echo %{_libdir}/phantomjs-qt > 0-phantomjs-qt-%{_arch}.conf

%install
rm -rf %{buildroot}
%{__install} -p -D -m 0755 bin/phantomjs %{buildroot}%{_bindir}/phantomjs
%{__install} -p -D -m 0644 0-phantomjs-qt-%{_arch}.conf %{buildroot}%{_sysconfdir}/ld.so.conf.d/0-phantomjs-qt-%{_arch}.conf
mkdir -p %{buildroot}%{_libdir}/phantomjs-qt
cp -a src/qt/lib/* %{buildroot}%{_libdir}/phantomjs-qt
rm -rf %{buildroot}%{_libdir}/phantomjs-qt/{fonts,pkgconfig,*.la,*.prl,README}

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/phantomjs
%{_libdir}/phantomjs-qt
%{_sysconfdir}/ld.so.conf.d/0-phantomjs-qt-%{_arch}.conf

%changelog
* Wed Jan 13 2013 Erik LaBianca <erik.labianca@gmail.com> - 1.8.1-1
- Update to 1.8.1 and port to epel-easel

* Wed Apr 18 2012 Simon Josi <me@yokto.net> - 1.5.0-1
- Package PhantomJS 1.5.0.
