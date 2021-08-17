%define		kdeframever	5.85
%define		qtver		5.9.0
%define		kfname		kdesignerplugin

Summary:	Framework for managing menu and toolbar actions
Name:		kf5-%{kfname}
Version:	5.85.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/portingAids/%{kfname}-%{version}.tar.xz
# Source0-md5:	6f09f3c76f6a698ede4fb67f6bb709cc
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.2.0
BuildRequires:	Qt5DBus-devel >= 5.2.0
BuildRequires:	Qt5Designer-devel >= 5.2.0
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5Network-devel >= 5.2.0
BuildRequires:	Qt5OpenGL-devel >= 5.3.1
BuildRequires:	Qt5Positioning-devel >= 5.3.1
BuildRequires:	Qt5PrintSupport-devel >= 5.3.1
BuildRequires:	Qt5Qml-devel >= 5.3.1
BuildRequires:	Qt5Quick-devel >= 5.3.1
BuildRequires:	Qt5Sensors-devel >= 5.3.1
BuildRequires:	Qt5WebKit-devel >= 5.3.1
BuildRequires:	Qt5Xml-devel >= 5.3.1
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kdewebkit-devel >= 5.59.0
BuildRequires:	kf5-kdoctools-devel >= %{version}
BuildRequires:	kf5-kglobalaccel-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kjobwidgets-devel >= %{version}
BuildRequires:	kf5-kplotting-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	qt5-linguist

BuildRequires:	cmake >= 2.8.12
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KXMLGUI provides a framework for managing menu and toolbar actions in
an abstract way. The actions are configured through a XML description
and hooks in the application code. The framework supports merging of
multiple description for example for integrating actions from plugins.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}5_qt --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5_qt.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/kgendesignerplugin
%{_mandir}/man1/kgendesignerplugin.1*
%lang(ca) %{_mandir}/ca/man1/kgendesignerplugin.1*
%lang(de) %{_mandir}/de/man1/kgendesignerplugin.1*
%lang(it) %{_mandir}/it/man1/kgendesignerplugin.1*
%lang(nl) %{_mandir}/nl/man1/kgendesignerplugin.1*
%lang(pt) %{_mandir}/pt/man1/kgendesignerplugin.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kgendesignerplugin.1*
%lang(sv) %{_mandir}/sv/man1/kgendesignerplugin.1*
%lang(uk) %{_mandir}/uk/man1/kgendesignerplugin.1*
%lang(es) %{_mandir}/es/man1/kgendesignerplugin.1.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KF5DesignerPlugin
