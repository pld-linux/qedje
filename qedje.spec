
%define		qtver	4.4.3

Summary:	qedje
Summary(pl.UTF-8):	qedje
Name:		qedje
Version:	0.3.0
Release:	0.1
License:	GPL v2
Group:		X11/Libraries
Source0:	http://dev.openbossa.org/%{name}/downloads/source/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	7435e3631fd44dce4086afe8698cdb13
URL:		http://dev.openbossa.org/trac/qedje
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	eet-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	qzion-devel
BuildRequires:	rpmbuild(macros) >= 1.164
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qedje

%description -l pl.UTF-8
qedje

%package devel
Summary:        Header files for qedje library
Summary(pl.UTF-8):      Pliki nag�~B처wkowe biblioteki qedje
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Header files for qedje library.

%description devel -l pl.UTF-8
Pliki nag�~B처wkowe biblioteki qedje.

%prep
%setup -q

%build
qmake-qt4 \
	PREFIX=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqedje.so.*.*.*
%attr(755,root,root) %{_libdir}/libqedje.prl
%attr(755,root,root) %ghost %{_libdir}/libqedje.so.?
%attr(755,root,root) %ghost %{_libdir}/libqedje.so.?.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqedje.so
%{_includedir}/*.h
%{_pkgconfigdir}/qedje.pc
