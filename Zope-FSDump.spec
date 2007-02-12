%define		zope_subname	FSDump
Summary:	Exports through-the-web objects (folders, DTML, etc.) as "natural" filesystem equivalents
Summary(pl.UTF-8):   Pakiet umożliwiający "zrzut" obiektów z Zope
Name:		Zope-%{zope_subname}
Version:	0.9.2
Release:	1
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://zope.org/Members/tseaver/%{zope_subname}/%{zope_subname}-%{version}/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	c8bb0b5fa3e04bfe1dfa811271e37871
URL:		http://zope.org/Members/tseaver/FSDump/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FSDump exports through-the-web objects (folders, DTML, etc.) as
"natural" filesystem equivalents.

%description -l pl.UTF-8
FSDump umożliwia "zrzut" obiektów z Zope.

%prep
%setup -q -n %{zope_subname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af FSDump/{help,interfaces,www,*.py,version.txt} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc FSDump/{CHANGES.txt,INSTALL.txt,README.txt,TODO.txt}
%{_datadir}/%{name}
