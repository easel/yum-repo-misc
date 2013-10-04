#!/bin/sh

version=$(rpm -q --specfile --qf='%{version}' nodejs-ansi.spec)
wget http://registry.npmjs.org/ansi/-/ansi-${version}.tgz
tar -zxf ansi-${version}.tgz
rm -f package/examples/imgcat/yoshi.png
tar -zcf ansi-${version}-stripped.tgz package
