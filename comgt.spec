Summary:	Controlling, configuring and interacting with Option Wireless 3G and 2G (HSDPA, UMTS, EDGE, GPRS, GSM) data devices
#Summary(pl.UTF-8):
Name:		comgt
Version:	0.32
Release:	1
License:	GPL v2
Group:		Utilities
Source0:	http://dl.sourceforge.net/comgt/%{name}.%{version}.tgz
# Source0-md5:	db2452680c3d953631299e331daf49ef
Source1:	%{name}-configure.ac
Source2:	%{name}-Makefile.am
Patch0:		%{name}-scriptdir.patch
URL:		http://sourceforge.net/projects/comgt
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Comgt is a command line tool for controlling, configuring and
interacting with Option Wireless 3G and 2G ( HSDPA, UMTS, EDGE, GPRS,
GSM) data devices within the Linux environment.

#description -l pl.UTF-8

%prep
%setup -q -n %{name}.%{version}
%patch -P0 -p1
cp -f %{SOURCE1} configure.ac
cp -f %{SOURCE2} Makefile.am 

%build
touch NEWS README AUTHORS ChangeLog
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG gprs.txt TODO umts.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*.1*
