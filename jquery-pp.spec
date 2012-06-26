%define		plugin	pp
Summary:	jQuery PP framework
Name:		jquery-%{plugin}
Version:	1.2.5
Release:	1
License:	MIT / GPL
Group:		Applications/WWW
Source0:	https://github.com/atirip/jquery.pp/tarball/%{version}/%{plugin}-%{version}.tgz
# Source0-md5:	ea7113eea93ddc84d74091377004fbe5
URL:		https://github.com/atirip/jquery.pp
BuildRequires:	js
BuildRequires:	rpmbuild(macros) > 1.268
BuildRequires:	closure-compiler
Requires:	jquery >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
This packages contains base jQuery PP framework

and additional optional plugins:
- jQuery Calendar plugin for PP framework
- jQuery Select plugin for PP framework

%prep
%setup -qc
mv *-jquery.%{plugin}-*/* .

%build
install -d build
# compress .js
for js in *.js; do
	# compress .js
	out=build/${js#jquery.}
	%if 0%{!?debug:1}
	closure-compiler --js $js --charset UTF-8 --js_output_file $out
	js -C -f $out
	%else
	cp -p $js $out
	%endif
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a build/* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_appdir}
