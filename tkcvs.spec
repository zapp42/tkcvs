Name:		tkcvs
Version:	7.2.2
Release:	2
Epoch:		0
Summary:	TkCVS and TkDiff

Group:		Development/Tools
License:	GPL
URL:		http://www.twobarleycorns.net/tkcvs.html
Source:		http://www.twobarleycorns.net/tkcvs_7_2_2.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	tk, tcl, cvs
BuildArch:	noarch

%description
TkCVS is a Tcl/Tk-based graphical interface to the CVS configuration
management system.  It displays the status of the files in the current
working directory, and provides buttons and menus to execute CVS
commands on the selected files. TkDiff is included for browsing and
merging your changes.

%prep
%setup -q -n tkcvs_7_2_2

%build
perl -pi -e 's|set TCDIR \[file join \$TclRoot tkcvs\]|set TCDIR "%{_datadir}/tkcvs"|' tkcvs/tkcvs.tcl
perl -pi -e 's|\[file join \$TclRoot tkcvs bitmaps\]|\[file join \$TCDIR bitmaps\]|' tkcvs/tkcvs.tcl

%install
install -d ${RPM_BUILD_ROOT}%{_datadir}
install -d ${RPM_BUILD_ROOT}%{_bindir}
install -d ${RPM_BUILD_ROOT}%{_mandir}/man1
cd tkcvs
install -m 0755 tkcvs.tcl ${RPM_BUILD_ROOT}%{_bindir}/tkcvs
rm -f tkcvs.blank mklocal mkmanpage.pl
install -m 0644 tkcvs.1 ${RPM_BUILD_ROOT}%{_mandir}/man1
cd ../tkdiff
install -m 0755 tkdiff ${RPM_BUILD_ROOT}%{_bindir}
cd ..
cp -fr tkcvs ${RPM_BUILD_ROOT}%{_datadir}
cp -fr bitmaps ${RPM_BUILD_ROOT}%{_datadir}/tkcvs

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_datadir}/tkcvs
%{_bindir}/*
%{_mandir}/man1/*
%doc CHANGELOG COPYING FAQ vendor5readme.pdf vendorcode.sh

%changelog
* Mon Feb 14 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:7.2.2-2
- Changed tk-devel and tcl-devel to tk and tcl
- Moved %%{_libdir}/tkcvs to %%{_datadir}/tkcvs

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:7.2.2-1
- New Version 7.2.2

* Sun May  2 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:7.2.1-0.fdr.1
- New Version 7.2.1

* Sun Jan  4 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:7.2-0.fdr.1
- New Version 7.2

* Wed Nov  5 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:7.1.4-0.fdr.1
- New Version 7.1.4

* Sun Oct 26 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:7.1.3-0.fdr.2
- Improved specfile

* Tue Oct 21 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:7.1.3-0.fdr.1
- New Version 7.1.3

* Sat Oct 18 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:7.1.2-0.fdr.1
- First Fedora release
