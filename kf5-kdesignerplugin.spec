%define		kdeframever	5.13
%define		qtver		5.3.2
%define		kfname		kdesignerplugin

Summary:	Framework for managing menu and toolbar actions
Name:		kf5-%{kfname}
Version:	5.13.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	8ac6b08151029fc148473325c90c8b4d
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
BuildRequires:	kf5-kdewebkit-devel >= %{version}
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
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{kfname}5_qt --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
# -f %{kfname}5_qt.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/kgendesignerplugin
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/kdewebkit5widgets.so
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/kf5widgets.so
%{_datadir}/kf5/widgets/pics/k3iconview.png
%{_datadir}/kf5/widgets/pics/k3listview.png
%{_datadir}/kf5/widgets/pics/kactionselector.png
%{_datadir}/kf5/widgets/pics/kactivelabel.png
%{_datadir}/kf5/widgets/pics/kcharselect.png
%{_datadir}/kf5/widgets/pics/kcmodule.png
%{_datadir}/kf5/widgets/pics/kcolorbutton.png
%{_datadir}/kf5/widgets/pics/kcolorcombo.png
%{_datadir}/kf5/widgets/pics/kcombobox.png
%{_datadir}/kf5/widgets/pics/kdatepicker.png
%{_datadir}/kf5/widgets/pics/kdatetable.png
%{_datadir}/kf5/widgets/pics/kdualcolorbutton.png
%{_datadir}/kf5/widgets/pics/kfontcombo.png
%{_datadir}/kf5/widgets/pics/kfontrequester.png
%{_datadir}/kf5/widgets/pics/kgradientselector.png
%{_datadir}/kf5/widgets/pics/khistorycombo.png
%{_datadir}/kf5/widgets/pics/khsselector.png
%{_datadir}/kf5/widgets/pics/kiconbutton.png
%{_datadir}/kf5/widgets/pics/kkeybutton.png
%{_datadir}/kf5/widgets/pics/kled.png
%{_datadir}/kf5/widgets/pics/klineedit.png
%{_datadir}/kf5/widgets/pics/klistbox.png
%{_datadir}/kf5/widgets/pics/kpalettetable.png
%{_datadir}/kf5/widgets/pics/kpasswordedit.png
%{_datadir}/kf5/widgets/pics/kruler.png
%{_datadir}/kf5/widgets/pics/ksqueezedtextlabel.png
%{_datadir}/kf5/widgets/pics/ktextedit.png
%{_datadir}/kf5/widgets/pics/kurlcomborequester.png
%{_datadir}/kf5/widgets/pics/kurllabel.png
%{_datadir}/kf5/widgets/pics/kurlrequester.png
%{_mandir}/man1/kgendesignerplugin.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KF5DesignerPlugin
