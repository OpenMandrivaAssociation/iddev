%define name iddev
%define version 1.9
%define release  %mkrel 1

Summary: Iddev is a library that identifies device contents
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Base
#Url: 


%description
iddev is a library that identifies device contents.  It will
tell you what file system (or logical volume manager) has
formatted the device.  This package contains the shared libraries.

%prep
%setup -q

%build
./configure --incdir=%{_includedir} \
	--kernel_src=/usr/src/linux \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--sbindir=%{_sbindir} \
	--sharedir=%{_datadir}/%name

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/libiddev.a
%{_includedir}/iddev.h

