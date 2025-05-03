#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Get the currently executing AST node of a frame, and other information
Summary(pl.UTF-8):	Pobieranie aktualnie wykonywanego węzła AST ramki oraz innych informacji
Name:		python3-executing
Version:	2.2.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/executing/
Source0:	https://files.pythonhosted.org/packages/source/e/executing/executing-%{version}.tar.gz
# Source0-md5:	6d79de70b73814ee0ac523140c47714f
URL:		https://pypi.org/project/executing/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
# for setuptools_scm[toml] >= ? with python3 < 3.11
BuildRequires:	python3-tomli >= 1
%if %{with tests}
BuildRequires:	python3-asttokens
BuildRequires:	python3-littleutils
BuildRequires:	python3-pytest
# py3.11+
#BuildRequires:	python3-rich
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This mini-package lets you get information about what a frame is
currently doing, particularly the AST node being executed.

%description -l pl.UTF-8
Ten minipakiet pozwala pobierać informacje o wykonywanej aktualnie
ramce, w szczególności węźle AST.

%prep
%setup -q -n executing-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%{py3_sitescriptdir}/executing
%{py3_sitescriptdir}/executing-%{version}-py*.egg-info
