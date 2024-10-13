%define major 2
%define libname %mklibname qtermwidget6
%define devname %mklibname qtermwidget6 -d
%define olddevname %mklibname qtermwidget -d
#define gitdate 20240419

Summary:	Qt terminal widget
Name:		qtermwidget
Version:	2.0.1
Release:	%{?gitdate:0.%{gitdate}.}2
License:	GPLv2+
Group:		Development/Other
Url:		https://github.com/lxqt/qtermwidget
Source0:	https://github.com/lxqt/qtermwidget/%{!?gitdate:releases/download/%{version}/qtermwidget-%{version}.tar.xz}%{?gitdate:archive/refs/heads/master.tar.gz#/%{name}-%{gitdate}.tar.gz}
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(lxqt2-build-tools)

%description
QTermWidget is an open source project based on KDE4 Konsole application.
The main goal of this project is to provide unicode-enabled,
embeddable Qt widget for using as a built-in console (or terminal
emulation widget).

%files
%{_datadir}/%{name}6/

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Qt terminal widget - shared library
Group:		System/Libraries
Requires:	%{name}

%description -n %{libname}
This package provides shared library for Qt4 terminal widget.

%files -n %{libname}
%{_libdir}/lib%{name}6.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Qt terminal widget - devel package
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Obsoletes:	%{name}-devel < 0.4.0-1
Provides:	%{name}-devel = %{EVRD}
%rename %{olddevname}

%description -n %{devname}
This package provides headers files for qtermwidget development.

%files -n %{devname}
%{_includedir}/%{name}6
%{_libdir}/lib%{name}6.so
%{_libdir}/pkgconfig/%{name}6.pc
%{_libdir}/cmake/%{name}6

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?gitdate:master}%{!?gitdate:%{version}}
%cmake -DUSE_QT6:BOOL=ON -DPULL_TRANSLATIONS=NO -DBUILD_DESIGNER_PLUGIN:BOOL=OFF -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
