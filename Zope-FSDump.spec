%define		zope_subname	FSDump
Summary:	Exports through-the-web objects (folders, DTML, etc.) as "natural" filesystem equivalents
Summary(pl):	Pakiet umo¿liwiaj±cy "zrzut" obiektów z Zope
Name:		Zope-%{zope_subname}
Version:	0.8.1
Release:	2
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://zope.org/Members/tseaver/%{zope_subname}/%{zope_subname}-%{version}/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	e9e57e1704387e4de022db7d6011abfb
URL:		http://zope.org/Members/tseaver/FSDump/
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FSDump exports through-the-web objects (folders, DTML, etc.) 
as "natural" filesystem equivalents.

%description -l pl
FSDump umo¿liwia "zrzut" obiektów z Zope.

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
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc FSDump/{CHANGES.txt,INSTALL.txt,README.txt,TODO.txt}
%{_datadir}/%{name}
