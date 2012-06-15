Name: usbutils
Version: 005
Release: 1
Source: http://downloads.sourceforge.net/linux-usb/%{name}-%{version}.tar.bz2
Source1001: packaging/usbutils.manifest
URL: http://www.linux-usb.org/
License: GPLv2+

BuildRequires: autoconf, libtool, pkgconfig(libusb-1.0)
Summary: Linux USB utilities
Group: Base/Tools

%description
This package contains utilities for inspecting devices connected to a
USB bus.

%prep
%setup -q

%build
cp %{SOURCE1001} .
%reconfigure \
	--datadir=%{_libdir}/usbutils

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} pkgconfigdir=/usr/share/pkgconfig

%docs_package

%files
%manifest usbutils.manifest
%defattr(-,root,root,-)
%{_sbindir}/*
%{_bindir}/*
%{_prefix}/share/*
%{_libdir}/usbutils/usb.ids
%doc AUTHORS COPYING ChangeLog NEWS README
