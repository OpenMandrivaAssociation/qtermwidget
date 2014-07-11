%define major 0
%define libname %mklibname qtermwidget %{major}
%define devname %mklibname qtermwidget -d

%define commit 8b3062f0248673b23b88afbd6f1d6ca581820c94
%define shortcommit %(c=%{commit}; echo ${c:0:7})

Summary:	Qt4 terminal widget
Name:		qtermwidget
Version:	0.4.0
Release: 	10
License:	GPLv2+
Group:		Development/Other
Url:		https://github.com/qterminal/qtermwidget/
#Source0:	https://github.com/qterminal/qtermwidget/archive/%{version}.tar.gz
Source0:	https://github.com/qterminal/qtermwidget/tarball/%{commit}/qterminal-%{name}-%{version}-%{shortcommit}.tar.gz
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist

%description
QTermWidget is an open source project based on KDE4 Konsole application.
The main goal of this project is to provide unicode-enabled,
embeddable QT4 widget for using as a built-in console (or terminal
emulation widget).

%files
%doc AUTHORS COPYING Changelog README TODO
%{_datadir}/%{name}/

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Qt4 terminal widget - shared library
Group:		System/Libraries
Requires:	%{name}

%description -n %{libname}
This package provides shared library for Qt4 terminal widget.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Qt4 terminal widget - devel package
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Obsoletes:	%{name}-devel < 0.4.0-1
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package provides headers files for qtermwidget development.

%files -n %{devname}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/qt4/plugins/designer/lib%{name}plugin.so

#----------------------------------------------------------------------------

%prep
%setup -qn qterminal-%{name}-%{shortcommit}

%build
%cmake
%make

%install
%makeinstall_std -C build

