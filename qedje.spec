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
BuildRequires:	eet
BuildRequires:	qzion
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qedje

%description -l pl.UTF-8
qedje

%prep
%setup -q

%build
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/plasma_applet_wifi_signal.so
