Summary:   spreadsheet based on sc, but with many enhancements
Name:      slsc
Version:   0.2.3
Release:   2
Copyright: GPL
Group:     Applications/Spreadsheets
Source:    ftp://space.mit.edu/pub/davis/slsc/slsc.tar.gz
Packager:  Tomsz K³oczko <kloczek@idk.com.pl>
Buildroot: /tmp/slsc-%{PACKAGE_VERSION}-root
%description
This is a much modified version of the public domain spread sheet sc, posted
several years ago by Mark Weiser as vc, originally by James Gosling. The
version that I have is based on Robert Bond's sc 6.1.  The latest version of
sc is 6.21.

%prep
%setup -n slsc

%build
./configure
make CFLAGS="$RPM_OPT_FLAGS" SLSC_ROOT=/usr/share/slsc SLSC_BIN=/usr/bin                                                            

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,share/slsc,man/man1}
cd src
make install	SLSC_ROOT=$RPM_BUILD_ROOT/usr/share/slsc \
		SLSC_BIN=$RPM_BUILD_ROOT/usr/bin
strip $RPM_BUILD_ROOT/usr/{bin/*,share/slsc/vprint}
install sc.doc $RPM_BUILD_ROOT/usr/man/man1/slsc.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README changes.txt
%attr(755, root, root) %dir /usr/share/slsc
%attr(644, root, root) /usr/share/slsc/slsc.*
%attr(644, root, root) /usr/share/slsc/tutorial.sc
%attr(755, root, root) /usr/share/slsc/vprint
%attr(755, root, root) /usr/bin/*
%attr(644, root, man) /usr/man/man1/*

%changelog
* Mon Nov 17 1997 Tomasz K³oczko <kloczek@idk.com.pl>        (0.2.3-2)
- added man page,
- spec file rewrited for using Buildroot,
- removed slsc-config.patch, added patch wit fixing Makefile.in and default
  slsc.rc,
- source changed to regular URL format,
- added %clean section,
- all files from /usr/lib/slsc moved to /usr/share/slsc,
- added %attr macros (allow build package from non root account).
* Tue Jun 24 1997 Scott Lampert <fortunato@heavymetal.org>   (0.2.3-1)
- previous not commented release in rpm.
