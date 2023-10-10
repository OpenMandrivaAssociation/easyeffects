Name:           easyeffects
Version:        7.1.0
Release:        1
Summary:        Audio equalizer, filters and effects for PipeWire applications
License:        GPLv3
Group:          Sound/Mixers
Url:            https://github.com/wwmm/easyeffects
Source0:        https://github.com/wwmm/easyeffects/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  appstream-util
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  libxml2-utils
BuildRequires:  meson
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(sigc++-3.0)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(sndfile)
BuildRewuires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(rnnoise)
BuildRequires:  pkgconfig(tbb)

BuildRequires:  libzita-convolver-devel

Requires:       gstreamer1.0-plugins-bad
Requires:       gstreamer1.0-plugins-good
Requires:       swh-plugins
Requires:       lsp-plugins
Requires:       %{_lib}rnnoise0
# Recommends because is optional and in contrib/unsupported repo
Recommends:     lv2-calf-plugins
Recommends:     rubberband
# Not packaged yet
Recommends:     mda-lv2
Recommends:     ladspa-zam-plugins
Recommends:     lv2-zam-plugins
Recommends:     zam-plugins

# Need for RNNoise
#Recommends: RNNoise

%description
This application was formerly known as PulseEffects, but it was renamed to Easy Effects after it started to use GTK4 and GStreamer usage was replaced by native PipeWire filters.
Limiters, compressor, reverberation, high-pass filter, low pass filter,
equalizer and auto volume effects for PipeWire applications.

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

desktop-file-install %{buildroot}%{_datadir}/applications/com.github.wwmm.%{name}.desktop \
    --add-category='X-OpenMandriva-CrossDesktop' \
    --dir=%{buildroot}%{_datadir}/applications

%find_lang %{name}
