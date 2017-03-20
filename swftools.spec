# Filter Python modules from Provides
%{?filter_setup:
%filter_provides_in %{python_sitearch}/.*\.so$
%filter_setup
}

Name:           swftools
Version:        0.9.2
Release:        5%{?dist}
Summary:        SWF manipulation and generation utilities

Group:          Applications/Multimedia
# swftools is GPLv2+ licensed, lib/MD5.c is BSD licensed,
# lib/action/actioncompiler.c is LGPLv2+ licensed
License:        GPLv3+ and LGPLv2+ and BSD
URL:            http://www.swftools.org/
Source0:        http://www.swftools.org/%{name}-%{version}.tar.gz
# Add prefix to installation paths
Patch0:         swftools-0.9.2-prefix.patch
# Fix installation
Patch1:         swftools-0.9.2-install.patch

BuildRequires:  fftw-devel
BuildRequires:  fontconfig-devel
BuildRequires:  giflib-devel
BuildRequires:  lame-devel
BuildRequires:  python-imaging-devel
BuildRequires:  zziplib-devel

%description
SWFTools is a collection of utilities for working with Adobe Flash files (SWF
files). The tool collection includes programs for reading SWF files, combining
them, and creating them from other content (like images, sound files, videos or
source code).


%package -n python-%{name}
Summary:        Python bindings for %{name}
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}

%description -n python-%{name}
This package provides Python bindings for %{name}.


%prep
%setup -q
%patch0 -p1 -b .prefix
%patch1 -p1 -b .install

# Fix permissions
chmod -x lib/*.[ch] lib/action/*.[ch]

# Fix encoding
for file in AUTHORS src/{jpeg2swf.1,swfstrings.1}; do
  iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
  touch -r $file $file.new && \
  mv $file.new $file
done


%build
export PYTHON_INCLUDES=$(python-config --includes)/Imaging/
export PYTHON_LIB=$(python-config --libs)
export PYTHON_LIB2=$PYTHON_LIB
export HAVE_PYTHON_IMAGING_LIB=1
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

install -dm 0755 $RPM_BUILD_ROOT%{python_sitearch}/
install -Dp lib/python/*.so $RPM_BUILD_ROOT%{python_sitearch}/


%files
%doc AUTHORS ChangeLog COPYING doc/fileformat.sc
%{_bindir}/*
%{_mandir}/man1/*.1.*
%{_datadir}/%{name}/


%files -n python-%{name}
%{python_sitearch}/*.so


%changelog
* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 01 2016 Sérgio Basto <sergio@serjux.com> - 0.9.2-4
-
  https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

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

* Thu Jan 10 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.1-3
- Remove pdflib-devel from BuildRequires

* Thu Nov 11 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.1-2
- Add missing BuildRequires fftw-devel and zziplib-devel
- Re-enable Python modules build

* Sun Jun 13 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> 0.9.1-1
- Update to 0.9.1
- Disable Python modules build (broken in 0.9.1)

* Wed Jun  3 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> 0.9.0-1
- Initial RPM release
