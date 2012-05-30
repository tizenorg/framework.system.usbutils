Name:           usbutils
Version:        0.86
Release:        6
License:        GPLv2+
Url:            http://www.linux-usb.org/
Source:         http://downloads.sourceforge.net/linux-usb/%{name}-%{version}.tar.gz
Source1001: packaging/usbutils.manifest 
Summary:        Linux USB utilities
Group:          Applications/System
#Source101:      usbutils-rpmlintrc
BuildRequires:  autoconf,
BuildRequires:  libtool,
BuildRequires:  pkgconfig(libusb) >= 0.1.8

%description
This package contains utilities for inspecting devices connected to a
USB bus.

%prep
%setup -q

%build
cp %{SOURCE1001} .
%reconfigure \
	--datadir=/usr/lib/usbutils

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} pkgconfigdir=/usr/share/pkgconfig

%docs_package

%files
%manifest usbutils.manifest
%defattr(-,root,root,-)
%{_sbindir}/*
%{_bindir}/*
%{_datadir}/pkgconfig/usbutils.pc
/usr/lib/usbutils/*
%doc COPYING

