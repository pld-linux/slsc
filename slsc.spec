Summary:	spreadsheet based on sc, but with many enhancements
Summary(pl):	Arkusz kalkulacyjny bazuj�cy na sc, ale z r�nymi rozszerzeniami
Name:		slsc
Version:	0.2.3
Release:	8
License:	GPL
Group:		Applications/Spreadsheets
Source0:	ftp://space.mit.edu/pub/davis/slsc/%{name}.tar.gz
Patch0:		%{name}.patch
Patch1:		%{name}-keymap.patch
Patch2:		%{name}-vprintpath.patch
BuildRequires:	slang-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a much modified version of the public domain spread sheet sc,
posted several years ago by Mark Weiser as vc, originally by James
Gosling. The version that I have is based on Robert Bond's sc 6.1. The
latest version of sc is 6.21.

%description -l pl
Jest to zmodyfikowana wersja dost�pnego jako public domain arkusza
kalkulacyjnego sc, wys�anego kilka lat temu przez Marka Weisera jako
vc, oryginalnie napisanego przez Jamesa Goslinga. Ta wersja bazuje na
wersji 6.1 sc Roberta Bonda.

%prep
%setup  -q -n slsc
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/slsc,%{_datadir}/slsc,%{_mandir}/man1}

%{__make} -C src install \
	SLSC_ROOT=$RPM_BUILD_ROOT%{_datadir}/slsc \
	SLSC_BIN=$RPM_BUILD_ROOT%{_bindir}

mv -f $RPM_BUILD_ROOT%{_datadir}/slsc/vprint $RPM_BUILD_ROOT%{_libdir}/slsc

install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/slsc
%attr(755,root,root) %{_libdir}/slsc/vprint
%dir %{_datadir}/slsc
%{_datadir}/slsc/slsc.*
%{_datadir}/slsc/tutorial.sc
%{_mandir}/man1/*
