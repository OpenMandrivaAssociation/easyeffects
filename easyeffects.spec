%global	_empty_manifest_terminate_build 0

Summary:	Audio equalizer, filters and effects for PipeWire applications
Name:	easyeffects
Version:	8.1.6
Release:	1
License:	GPLv3+
Group:	Sound/Mixers
Url:	https://github.com/wwmm/easyeffects
Source0:	https://github.com/wwmm/easyeffects/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	breeze-icons
BuildRequires:	cmake >= 3.28
BuildRequires:	desktop-file-utils
BuildRequires:	extra-cmake-modules
BuildRequires:	gettext
BuildRequires:	itstool
#BuildRequires:	kf6-kirigami-addons-devel
BuildRequires:	%{_lib}omp
BuildRequires:	%{_lib}Qt6LabsSynchronizer
BuildRequires:	%{_lib}tbbind
BuildRequires:	libxml2-utils
BuildRequires:	make
BuildRequires:	cmake(KF6ColorScheme)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Kirigami)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KF6QQC2DesktopStyle)
BuildRequires:	boost-devel
BuildRequires:	gomp-devel
BuildRequires:	ladspa-devel
BuildRequires:	libzita-convolver-devel
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(fmt)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(libebur128) >= 1.2.6
BuildRequires:	pkgconfig(libpipewire-0.3) >= 1.0.6
BuildRequires:	pkgconfig(libportal-qt6)
BuildRequires:	pkgconfig(lilv-0)
BuildRequires:	pkgconfig(lv2) >= 1.18.2
BuildRequires:	pkgconfig(nlohmann_json)
BuildRequires:	pkgconfig(Qt6Core) >= 6.10.2
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Graphs)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:	pkgconfig(Qt6QmlCompiler)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6QuickControls2)
BuildRequires:	pkgconfig(Qt6WebEngineCore)
BuildRequires:	pkgconfig(Qt6WebEngineQuick)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(rnnoise)
BuildRequires:	pkgconfig(sigc++-3.0)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(soundtouch)
BuildRequires:	pkgconfig(speexdsp)
BuildRequires:	pkgconfig(tbb)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:pkgconfig(webrtc-audio-processing-2)
BuildRequires:	pkgconfig(xkbcommon)
Requires:	gstreamer1.0-plugins-bad
Requires:	gstreamer1.0-plugins-good
Requires:	%{_lib}rnnoise0
Requires:	lsp-plugins
Requires:	swh-plugins
# Recommended because optional and in Extra repo
Recommends:	calf
Recommends:	lv2-calf-plugins
Recommends:	mda-lv2
Recommends:	rubberband
Recommends:	zam-plugins
Recommends:	zam-plugins-ladspa
Recommends:	zam-plugins-lv2

%description
Limiters, compressor, reverberation, high-pass filter, low pass filter,
equalizer and auto volume effects for PipeWire applications.
This application was formerly known as PulseEffects, but it was renamed to
Easy Effects after it started to use GTK4 and GStreamer usage was replaced by
native PipeWire filters. Now the whole application was ported from GTK4 to a
combination of Qt, QML and KDE/Kirigami frameworks.

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/com.github.wwmm.%{name}.desktop
#{_datadir}/dbus-1/services/com.github.wwmm.%%{name}.service
#{_datadir}/glib-2.0/schemas/com.github.wwmm.%%{name}.*
#{_datadir}/help/C/%%{name}/
%{_datadir}/metainfo/com.github.wwmm.%{name}.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/com.github.wwmm.%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/com.github.wwmm.%{name}-symbolic.svg

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
export LC_ALL="${LC_ALL:-UTF-8}"
%cmake
%make_build


%install
export LC_ALL="${LC_ALL:-UTF-8}"
%make_install -C build

desktop-file-edit --add-category='X-OpenMandriva-CrossDesktop' \
		%{buildroot}%{_datadir}/applications/com.github.wwmm.%{name}.desktop

%find_lang %{name}
#find_lang %%{name}-news
#cat %%{name}-news.lang >> %%{name}.lang
