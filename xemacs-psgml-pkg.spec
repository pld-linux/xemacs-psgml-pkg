Summary: 	Validated HTML/SGML editing
Summary(pl):	Tryb edycji HTML/SGML
Name:    	xemacs-psgml-pkg
%define 	srcname	psgml
Version: 	1.14
Release:	1
Copyright:	GPL
Group:    	Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
URL:      	http://www.xemacs.org
Source:   	ftp://ftp.xemacs.org/packages/%{srcname}-%{version}-pkg.tar.gz
Patch:		xemacs-psgml-pkg-info.patch
Prereq:		/usr/sbin/fix-info-dir
Conflicts:	xemacs-sumo
Requires: 	xemacs
Requires: 	xemacs-edit-utils-pkg
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch
Obsoletes:	psgml

%description
PSGML is a major mode for editing SGML documents for XEmacs and Emacs.

%description -l pl 
PSGML jest g³ownym trybem edysji dokumentów SGML dla XEmacsa i Emacsa.

%package el
Summary: 	Validated HTML/SGML editing. This package contains .el files
Summary(pl):	Validated HTML/SGML editing. Pliki ¿ród³owe .el
Group:    	Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires: 	%{name} = %{version}

%description el
.el source files -- not necessary to run XEmacs.

%description el -l pl
Pliki ¼ród³owe procedur w eLispie do XEmacsa.

%prep
%setup -q -c
%patch -p1

%build
(cd man/psgml; makeinfo psgml-api.texi psgml.texi )

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a etc lisp $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
install info/*.info* $RPM_BUILD_ROOT%{_infodir}

rm -f $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/psgml/ChangeLog

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info \
	lisp/psgml/ChangeLog \
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/psgml/*.el

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc lisp/psgml/ChangeLog.gz
%{_infodir}/*
%{_datadir}/xemacs-packages/etc/*
%dir %{_datadir}/xemacs-packages/lisp/psgml
%{_datadir}/xemacs-packages/lisp/psgml/*.elc

%files el
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/lisp/psgml/*.el.gz
