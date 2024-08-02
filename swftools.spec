%global commit 772e55a271f66818b06c6e8c9b839befa51248f4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20211216

# Disable parallel build to avoid compilation issues
%global _smp_mflags %{nil}

Name:           swftools
Version:        0.9.2^%{commitdate}git%{shortcommit}
Release:        2%{?dist}
Summary:        SWF manipulation and generation utilities

# swftools is GPL-2.0-or-later licensed, some libraries are LGPL-2.0-or-later/GPL-3.0-or-later
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later
URL:            http://www.swftools.org/
Source0:        https://github.com/matthiaskramm/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  fftw-devel
BuildRequires:  fontconfig-devel
BuildRequires:  gcc-c++
BuildRequires:  freetype-devel
BuildRequires:  giflib-devel
BuildRequires:  lame-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  perl-interpreter
BuildRequires:  zlib-devel
BuildRequires:  zziplib-devel

%description
SWFTools is a collection of utilities for working with Adobe Flash files (SWF
files). The tool collection includes programs for reading SWF files, combining
them, and creating them from other content (like images, sound files, videos or
source code).


%prep
%autosetup -n %{name}-%{commit}

# Remove the bundled LAME library to ensure the build tools search for and use
# the system's LAME library instead.
rm -r lib/lame/

# Fix encoding
for file in AUTHORS COPYING src/{jpeg2swf.1,swfstrings.1}; do
  iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
  touch -r $file $file.new && \
  mv $file.new $file
done


%build
%configure
%make_build \


%install
%make_install \
  bindir=$RPM_BUILD_ROOT%{_bindir} \
  datadir=$RPM_BUILD_ROOT%{_datadir} \
  libdir=$RPM_BUILD_ROOT%{_libdir} \
  mandir=$RPM_BUILD_ROOT%{_mandir}

# Fix absolute symlinks
ln -sf tessel_loader.swf $RPM_BUILD_ROOT%{_datadir}/%{name}/swfs/default_loader.swf
ln -sf simple_viewer.swf $RPM_BUILD_ROOT%{_datadir}/%{name}/swfs/default_viewer.swf


%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*.1.*
%{_datadir}/%{name}/


%changelog
* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.9.2^20211216git772e55a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 10 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.2^20211216git772e55a-1
- Update to latest snapshot

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.9.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.9.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.2-16
- Fix build with GCC 11

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.2-13
- Drop Python 2 module
- Spec cleanup

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.9.2-9
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.2-7
- Spec cleanup
- Update for latest Python guidelines
- Fix build with giflib >= 5

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 01 2016 Sérgio Basto <sergio@serjux.com> - 0.9.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.9.2-2
- Mass rebuilt for Fedora 19 Features

* Tue Apr 10 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.9.1-6
- Rebuilt for c++ ABI breakage

* Tue Jan 24 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.1-5
- Fix License tag

* Wed Nov 30 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.1-4
- Spec cleanup

* Mon Jan 10 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.1-3
- Remove pdflib-devel from BuildRequires

* Thu Nov 11 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.1-2
- Add missing BuildRequires fftw-devel and zziplib-devel
- Re-enable Python modules build

* Sun Jun 13 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> 0.9.1-1
- Update to 0.9.1
- Disable Python modules build (broken in 0.9.1)

* Thu Jun  3 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> 0.9.0-1
- Initial RPM release
