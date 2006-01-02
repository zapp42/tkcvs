Name:		tkcvs
Version:	8.0
Release:	1%{?dist}

Summary:	TkCVS and TkDiff

Group:		Development/Tools
License:	GPL
URL:		http://www.twobarleycorns.net/tkcvs.html
Source:		http://www.twobarleycorns.net/tkcvs_8_0.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	tk, tcl, cvs
BuildArch:	noarch

%description
TkCVS is a Tcl/Tk-based graphical interface to the CVS and Subversion
configuration management systems. It will also help with RCS. TkDiff
is included for browsing and merging your changes.

TkCVS shows the status of the files in the current working directory,
and has tools for tagging, merging, importing, exporting, checking
in/out, and other user operations.

TkCVS also aids in browsing the repository. For Subversion, the
repository tree is browsed like an ordinary file tree. For CVS, the
CVSROOT/modules file is read. TkCVS extends CVS with a method to
produce a "user friendly" listing of modules. This requires special
comments in the CVSROOT/modules file.

Although TkCVS now supports Subversion, it will still work happily
without it in your CVS directories. It didn't abandon CVS, it just
grew some new capabilities.


%prep
%setup -q -n tkcvs_8_0


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

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc CHANGELOG COPYING FAQ vendor5readme.pdf vendorcode.sh
%{_datadir}/tkcvs
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Jan  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 8.0
- new version 8.0

* Sat Aug 13 2005 Gerard Milmeister <gemi@bluewin.ch> - 7.2.4
- new version 7.2.4

* Tue Jul  5 2005 Gerard Milmeister <gemi@bluewin.ch> - 7.2.3-1
- new version 7.2.3

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

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
