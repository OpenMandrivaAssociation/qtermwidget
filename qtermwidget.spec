%define major	0
%define	libname		%mklibname qtermwidget %{major}
%define	devname	%mklibname -d qtermwidget

%define commit 8b3062f0248673b23b88afbd6f1d6ca581820c94
%define shortcommit %(c=%{commit}; echo ${c:0:7})


Summary:	Qt4 terminal widget
Name:		qtermwidget
Version:	0.4.0
Release: 	6
License:	GPLv2
Group:		Development/Other
URL:            https://github.com/qterminal/qtermwidget/
#Source0:       https://github.com/qterminal/qtermwidget/archive/%{version}.tar.gz
Source0:        https://github.com/qterminal/qtermwidget/tarball/%{commit}/qterminal-%{name}-%{version}-%{shortcommit}.tar.gz
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist

%description
QTermWidget is an open source project based on KDE4 Konsole application. 
The main goal of this project is to provide unicode-enabled, 
embeddable QT4 widget for using as a built-in console (or terminal 
emulation widget). 

%package -n 	%{libname}
Summary:	Qt4 terminal widget - devel package
Group:          System/Libraries
Requires:       %{name} >= %{version}-%{release}

%description -n %{libname}
This package provides headers files for qtermwidget development.

%package -n %{devname}
Summary:	Qt4 terminal widget - devel package
Group:          Development/Other
Requires:       %{name} >= %{version}-%{release}
Obsoletes:	%{name}-devel < 0.4.0-1
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package provides headers files for qtermwidget development.

%prep
%setup -qn qterminal-%{name}-%{shortcommit}

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%doc AUTHORS COPYING Changelog INSTALL README TODO
%{_datadir}/%{name}/

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/qt4/plugins/designer/lib%{name}plugin.so

