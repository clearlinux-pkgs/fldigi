#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fldigi
Version  : 4.0.16
Release  : 9
URL      : https://sourceforge.net/projects/fldigi/files/fldigi/fldigi-4.0.16.tar.gz
Source0  : https://sourceforge.net/projects/fldigi/files/fldigi/fldigi-4.0.16.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: fldigi-bin
Requires: fldigi-data
Requires: fldigi-locales
Requires: fldigi-doc
BuildRequires : alsa-lib-dev
BuildRequires : asciidoc
BuildRequires : fltk-dev
BuildRequires : fontconfig-dev
BuildRequires : hamlib-dev
BuildRequires : libXcursor-dev
BuildRequires : libXft-dev
BuildRequires : libXinerama-dev
BuildRequires : libXrender-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libsndfile-dev
BuildRequires : pkgconfig(portaudio-2.0)
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(xext)
BuildRequires : pulseaudio-dev

%description
Fldigi is a software modem for Amateur Radio use. It is a sound card based
program that is used for both transmitting and receiving data in any of the
following modes:

%package bin
Summary: bin components for the fldigi package.
Group: Binaries
Requires: fldigi-data

%description bin
bin components for the fldigi package.


%package data
Summary: data components for the fldigi package.
Group: Data

%description data
data components for the fldigi package.


%package doc
Summary: doc components for the fldigi package.
Group: Documentation

%description doc
doc components for the fldigi package.


%package locales
Summary: locales components for the fldigi package.
Group: Default

%description locales
locales components for the fldigi package.


%prep
%setup -q -n fldigi-4.0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518198873
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1518198873
rm -rf %{buildroot}
%make_install
%find_lang fldigi

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flarq
/usr/bin/fldigi

%files data
%defattr(-,root,root,-)
/usr/share/applications/flarq.desktop
/usr/share/applications/fldigi.desktop
/usr/share/fldigi/NAVTEX_Stations.csv
/usr/share/fldigi/ToR-Stats-SHIP.csv
/usr/share/fldigi/nsd_bbsss.txt
/usr/share/fldigi/station_table.txt
/usr/share/pixmaps/flarq.xpm
/usr/share/pixmaps/fldigi.xpm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files locales -f fldigi.lang
%defattr(-,root,root,-)

