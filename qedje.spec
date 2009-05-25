
%define		qtver	4.5.0

Summary:	qedje
Summary(pl.UTF-8):	qedje
Name:		qedje
Version:	0.4.0
Release:	0.git.2
License:	GPL v2
Group:		X11/Libraries
#Source0:	http://dev.openbossa.org/%{name}/downloads/source/%{name}/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}-git.tar.gz
# Source0-md5:	062a73e4ce76ae4513aa772504db572d
URL:		http://dev.openbossa.org/trac/qedje
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	eet-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	qzion-devel >= 0.4.0
BuildRequires:	rpmbuild(macros) >= 1.164
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qedje

%description -l pl.UTF-8
qedje

%package devel
Summary:        Header files for qedje library
Summary(pl.UTF-8):      Pliki nagłówkowe biblioteki qedje
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Header files for qedje library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki qedje.

%prep
%setup -q -n %{name}-%{version}-git

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qedje_viewer
%attr(755,root,root) %{_libdir}/libqedje.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqedje.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqedje.so
%{_includedir}/*.h
%{_pkgconfigdir}/qedje.pc
