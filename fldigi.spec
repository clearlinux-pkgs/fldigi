#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fldigi
Version  : 4.1.18
Release  : 32
URL      : https://sourceforge.net/projects/fldigi/files/fldigi/fldigi-4.1.18.tar.gz
Source0  : https://sourceforge.net/projects/fldigi/files/fldigi/fldigi-4.1.18.tar.gz
Summary  : Library to access network sites using https protocol
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: fldigi-bin = %{version}-%{release}
Requires: fldigi-data = %{version}-%{release}
Requires: fldigi-license = %{version}-%{release}
Requires: fldigi-locales = %{version}-%{release}
Requires: fldigi-man = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : asciidoc
BuildRequires : fltk-dev
BuildRequires : fontconfig-dev
BuildRequires : hamlib-dev
BuildRequires : libXcursor-dev
BuildRequires : libXft-dev
BuildRequires : libXrender-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libsndfile-dev
BuildRequires : pkgconfig(portaudio-2.0)
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pulseaudio-dev
Patch1: CVE-2019-16910.patch

%description
Fldigi is a software modem for Amateur Radio use. It is a sound card based
program that is used for both transmitting and receiving data in any of the
following modes:

%package bin
Summary: bin components for the fldigi package.
Group: Binaries
Requires: fldigi-data = %{version}-%{release}
Requires: fldigi-license = %{version}-%{release}

%description bin
bin components for the fldigi package.


%package data
Summary: data components for the fldigi package.
Group: Data

%description data
data components for the fldigi package.


%package license
Summary: license components for the fldigi package.
Group: Default

%description license
license components for the fldigi package.


%package locales
Summary: locales components for the fldigi package.
Group: Default

%description locales
locales components for the fldigi package.


%package man
Summary: man components for the fldigi package.
Group: Default

%description man
man components for the fldigi package.


%prep
%setup -q -n fldigi-4.1.18
cd %{_builddir}/fldigi-4.1.18
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611955459
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --enable-optimizations=sse3 --enable-debug
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1611955459
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fldigi
cp %{_builddir}/fldigi-4.1.18/COPYING %{buildroot}/usr/share/package-licenses/fldigi/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/fldigi-4.1.18/src/mbedtls/LICENSE %{buildroot}/usr/share/package-licenses/fldigi/941df1b3181ce17b8441e0e3775808f266a80fc8
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fldigi/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/fldigi/941df1b3181ce17b8441e0e3775808f266a80fc8

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/flarq.1
/usr/share/man/man1/fldigi.1

%files locales -f fldigi.lang
%defattr(-,root,root,-)

