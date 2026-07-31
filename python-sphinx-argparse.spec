%global upname sphinx-argparse
%global srcname sphinx_argparse

Name: python-%{upname}
Version: 0.6.0
Release: 1
Summary: Sphinx extension that automatically documents argparse commands and options
BuildArch: noarch

License: MIT
Url: https://github.com/ashb/sphinx-argparse
Source0: https://files.pythonhosted.org/packages/source/s/sphinx-argparse/sphinx_argparse-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3dist(lxml)

BuildSystem: python

%description
Sphinx extension that automatically documents argparse commands and options

%prep
%autosetup -n sphinx_argparse-0.6.0 -p1

%files
%license LICENCE.rst
%doc README.rst
%{python3_sitelib}/sphinx_argparse-%{version}.dist-info
%{python3_sitelib}/sphinxarg/
