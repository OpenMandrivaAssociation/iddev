%define name iddev
%define version 1.9
%define release  %mkrel 6

Summary: Library that identifies device contents
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Base
#Url: 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9-6mdv2011.0
+ Revision: 619600
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.9-5mdv2010.0
+ Revision: 429495
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.9-4mdv2009.0
+ Revision: 247201
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.9-2mdv2008.1
+ Revision: 170893
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.9-1mdv2008.1
+ Revision: 131677
- fix group
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- fix summary-ended-with-dot
- import iddev


* Mon Apr 11 2005 Antoine Giniès <aginies@mandriva.com> 1.9-1mdk
- first release
