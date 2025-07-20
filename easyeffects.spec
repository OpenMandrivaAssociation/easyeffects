%global	_empty_manifest_terminate_build 0

Summary:	Audio equalizer, filters and effects for PipeWire applications
Name:	easyeffects
Version:	7.2.5
Release:	1
License:	GPLv3+
Group:	Sound/Mixers
Url:	https://github.com/wwmm/easyeffects
Source0:	https://github.com/wwmm/easyeffects/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	appstream-util
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	meson
BuildRequires:	boost-devel
BuildRequires:	ladspa-devel
BuildRequires:	libzita-convolver-devel
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(fmt)
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(libebur128)
BuildRequires:	pkgconfig(libpipewire-0.3) >= 0.3.58
BuildRequires:	pkgconfig(libportal-gtk4)
BuildRequires:	pkgconfig(lilv-0)
BuildRequires:	pkgconfig(lv2) >= 1.18.2
BuildRequires:	pkgconfig(nlohmann_json)
BuildRequires:	pkgconfig(rnnoise)
BuildRequires:	pkgconfig(sigc++-3.0)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(soundtouch)
BuildRequires:	pkgconfig(speexdsp)
BuildRequires:	pkgconfig(tbb)
Requires:	gstreamer1.0-plugins-bad
Requires:	gstreamer1.0-plugins-good
Requires:	%{_lib}rnnoise0
Requires:	lsp-plugins
Requires:	swh-plugins
# Recommended because optional and in Extra/unsupported repo
Recommends:	calf
Recommends:	lv2-calf-plugins
Recommends:	mda-lv2
Recommends:	rubberband
Recommends:	zam-plugins
Recommends:	zam-plugins-ladspa
Recommends:	zam-plugins-lv2

# Need for RNNoise
#Recommends: RNNoise

%description
Limiters, compressor, reverberation, high-pass filter, low pass filter,
equalizer and auto volume effects for PipeWire applications.
This application was formerly known as PulseEffects, but it was renamed to
Easy Effects after it started to use GTK4 and GStreamer usage was replaced by
native PipeWire filters.

%files -f easyeffects.lang
%{_bindir}/%{name}
%{_datadir}/applications/com.github.wwmm.%{name}.desktop
%{_datadir}/dbus-1/services/com.github.wwmm.%{name}.service
%{_datadir}/glib-2.0/schemas/com.github.wwmm.%{name}.*
%{_datadir}/help/C/%{name}/
%{_datadir}/metainfo/com.github.wwmm.%{name}.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/com.github.wwmm.%{name}.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.github.wwmm.%{name}-symbolic.svg

#-----------------------------------------------------------------------------

%prep
%autosetup -p1
rm -rf build && mkdir build


%build
export LC_ALL="${LC_ALL:-UTF-8}"
cd build
meson --prefix=/usr ..
%ninja_build
cd ..


%install
export LC_ALL="${LC_ALL:-UTF-8}"
cd build
%ninja_install
cd ..

desktop-file-edit --add-category='X-OpenMandriva-CrossDesktop' \
		%{buildroot}%{_datadir}/applications/com.github.wwmm.%{name}.desktop

%find_lang %{name}
%find_lang %{name}-news
cat %{name}-news.lang >> %{name}.lang
