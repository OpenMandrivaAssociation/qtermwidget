%define major 0
%define libname %mklibname qtermwidget5 %{major}
%define devname %mklibname qtermwidget5 -d
%define olddevname %mklibname qtermwidget -d

%define commit 0b430bfd9209a0ad4e48b658475d1113240637ab
%define shortcommit %(c=%{commit}; echo ${c:0:7})

Summary:	Qt terminal widget
Name:		qtermwidget
Version:	0.6.0
Release: 	1
License:	GPLv2+
Group:		Development/Other
Url:		https://github.com/lxde/qtermwidget
Source0:	https://github.com/lxde/qtermwidget/releases/download/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	qt5-linguist

%description
QTermWidget is an open source project based on KDE4 Konsole application.
The main goal of this project is to provide unicode-enabled,
embeddable Qt widget for using as a built-in console (or terminal
emulation widget).

%files
%doc AUTHORS COPYING Changelog README TODO
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
%{_datadir}/cmake/%{name}5

#----------------------------------------------------------------------------

%prep
%setup -qn qterminal-%{name}-%{shortcommit}
%apply_patches

%build
%cmake_qt5 -DUSE_QT5:BOOL=ON -DBUILD_DESIGNER_PLUGIN:BOOL=OFF
%make

%install
%makeinstall_std -C build

