%define major 0
%define libname %mklibname qtermwidget5 %{major}
%define devname %mklibname qtermwidget5 -d
%define olddevname %mklibname qtermwidget -d

Summary:	Qt terminal widget
Name:		qtermwidget
Version:	0.14.1
Release: 	2
License:	GPLv2+
Group:		Development/Other
Url:		https://github.com/lxde/qtermwidget
Source0:	https://github.com/lxde/qtermwidget/archive/%{version}.tar.gz
Patch0:		qtermwidget-0.14.1-fix-build.patch
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(lxqt-build-tools)

%description
QTermWidget is an open source project based on KDE4 Konsole application.
The main goal of this project is to provide unicode-enabled,
embeddable Qt widget for using as a built-in console (or terminal
emulation widget).

%files
%{_datadir}/%{name}5/

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Qt terminal widget - shared library
Group:		System/Libraries
Requires:	%{name}

%description -n %{libname}
This package provides shared library for Qt4 terminal widget.

%files -n %{libname}
%{_libdir}/lib%{name}5.so.%{major}*

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
%{_includedir}/%{name}5
%{_libdir}/lib%{name}5.so
%{_libdir}/pkgconfig/%{name}5.pc
%{_libdir}/cmake/%{name}5

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake_qt5 -DUSE_QT5:BOOL=ON -DPULL_TRANSLATIONS=NO -DBUILD_DESIGNER_PLUGIN:BOOL=OFF
%make_build

%install
%make_install -C build
