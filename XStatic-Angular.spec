#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Angular
Version  : 1.5.8.0
Release  : 18
URL      : http://pypi.debian.net/XStatic-Angular/XStatic-Angular-1.5.8.0.tar.gz
Source0  : http://pypi.debian.net/XStatic-Angular/XStatic-Angular-1.5.8.0.tar.gz
Summary  : Angular 1.5.8 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT MPL-2.0
Requires: XStatic-Angular-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
XStatic-Angular
---------------
Angular JavaScript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-Angular package.
Group: Default
Provides: xstatic-angular-python

%description python
python components for the XStatic-Angular package.


%prep
%setup -q -n XStatic-Angular-1.5.8.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488595364
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1488595364
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
