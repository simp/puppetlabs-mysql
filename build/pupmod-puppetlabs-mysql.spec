Summary: Puppet Labs MySQL Module
Name: pupmod-puppetlabs-mysql
Version: 2.2.3
Release: 1
License: Apache License 2.0
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: puppetlabs-stdlib >= 3.2.0
Requires: pupmod-iptables >= 4.1.0-4
Buildarch: noarch
Requires: simp-bootstrap >= 4.2.0
Obsoletes: pupmod-puppetlabs-mysql-test

Prefix: /etc/puppet/environments/simp/modules

%description
This is the puppetlabs MySQL module hosted at
https://github.com/puppetlabs/puppetlabs-mysql

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/mysql

dirs='files lib manifests templates'
for dir in $dirs; do
  test -d $dir && cp -r $dir %{buildroot}/%{prefix}/mysql
done

cp Modulefile %{buildroot}/%{prefix}/mysql
cp README.md %{buildroot}/%{prefix}/mysql
cp TODO %{buildroot}/%{prefix}/mysql
cp CHANGELOG.md %{buildroot}/%{prefix}/mysql
cp Gemfile %{buildroot}/%{prefix}/mysql
cp LICENSE %{buildroot}/%{prefix}/mysql
cp metadata.json %{buildroot}/%{prefix}/mysql

mkdir -p %{buildroot}/usr/share/simp/tests/modules/mysql

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/mysql

%files
%defattr(0640,root,puppet,0750)
%{prefix}/mysql

%post
#!/bin/sh

if [ -d %{prefix}/mysql/plugins ]; then
  /bin/mv %{prefix}/mysql/plugins %{prefix}/mysql/plugins.bak
fi

%postun
# Post uninstall stuff

%changelog
* Fri Feb 13 2015 - Trevor Vaughan <tvaughan@onyxpoint.com> - 2.2.3-1
- Migrated to the new 'simp' environment

* Wed May 14 2014 Nick Markowski <nmarkowski@keywcorp.com> - 2.2.3-0
- Incorporated and packaged module from github repository
