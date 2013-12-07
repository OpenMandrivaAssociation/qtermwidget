%define major	0

%define	libname		%mklibname qtermwidget %{major}
%define	develname	%mklibname -d qtermwidget

Name:		qtermwidget
Summary:	Qt4 terminal widget
Version:	0.4.0
Release: 	3
License:	GPLv2
Source0:	%{name}-%{name}-master.tar.gz
Group:		Development/Other
URL:		https://gitorious.org/qtermwidget
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist

Summary:	Qt4 terminal widget

%description
QTermWidget is an open source project based on KDE4 Konsole application. 
The main goal of this project is to provide unicode-enabled, 
embeddable QT4 widget for using as a built-in console (or terminal 
emulation widget). 

%package -n 	%libname
Summary:	Qt4 terminal widget - devel package
Group:          System/Libraries
Requires:       %{name} >= %{version}-%{release}

%description -n %libname
This package provides headers files for qtermwidget development.

%package -n %develname
Summary:	Qt4 terminal widget - devel package
Group:          Development/Other
Requires:       %{name} >= %{version}-%{release}
Obsoletes:	%{name}-devel < 0.4.0-1
Provides:	%{name}-devel = %{version}-%{release}

%description -n %develname
This package provides headers files for qtermwidget development.

%prep
%setup -q -n %{name}-%{name}

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%doc AUTHORS COPYING Changelog INSTALL README TODO
%{_datadir}/%{name}/

%files -n %libname
%{_libdir}/lib%{name}.so.%{major}*

%files -n %develname
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/qt4/plugins/designer/lib%{name}plugin.so
