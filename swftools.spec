Name:           swftools
Version:        0.9.2
Release:        8%{?dist}
Summary:        SWF manipulation and generation utilities

Group:          Applications/Multimedia
# swftools is GPLv2+ licensed, lib/MD5.c is BSD licensed,
# lib/action/actioncompiler.c is LGPLv2+ licensed
License:        GPLv3+ and LGPLv2+ and BSD
URL:            http://www.swftools.org/
Source0:        http://www.swftools.org/%{name}-%{version}.tar.gz
# Fix installation
Patch0:         swftools-0.9.2-install.patch
# Fix build with giflib >= 5
Patch1:         swftools-0.9.2-giflib5.patch

BuildRequires:  fftw-devel
BuildRequires:  fontconfig-devel
BuildRequires:  giflib-devel
BuildRequires:  lame-devel
BuildRequires:  python2-devel
BuildRequires:  python2-pillow-devel
BuildRequires:  zziplib-devel

%description
SWFTools is a collection of utilities for working with Adobe Flash files (SWF
files). The tool collection includes programs for reading SWF files, combining
them, and creating them from other content (like images, sound files, videos or
source code).


%package -n python2-%{name}
Summary:        Python bindings for %{name}
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
This package provides Python bindings for %{name}.


%prep
%autosetup -p0

# Fix permissions
chmod -x lib/*.[ch] lib/action/*.[ch]

# Fix encoding
for file in AUTHORS src/{jpeg2swf.1,swfstrings.1}; do
  iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
  touch -r $file $file.new && \
  mv $file.new $file
done


%build
export PYTHON_INCLUDES=$(python2-config --includes)/Imaging/
export PYTHON_LIB=$(python2-config --libs)
export PYTHON_LIB2=$PYTHON_LIB
export HAVE_PYTHON_IMAGING_LIB=1
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

install -dm 0755 $RPM_BUILD_ROOT%{python2_sitearch}/
install -Dp lib/python/*.so $RPM_BUILD_ROOT%{python2_sitearch}/


%files
%doc AUTHORS ChangeLog doc/fileformat.sc
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*.1.*
%{_datadir}/%{name}/


%files -n python2-%{name}
%{python_sitearch}/*.so


%changelog
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
