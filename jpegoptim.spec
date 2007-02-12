Summary:	Utility for optimizing and compressing JPEG files.
Summary(pl.UTF-8):   Program do optymalizacji i kompresji plików JPEG.
Name:		jpegoptim
Version:	1.2.2
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.cc.jyu.fi/~tjko/src/%{name}-%{version}.tar.gz
# Source0-md5:	c7e92417badac7dcffab4245c113871c
URL:		http://www.iki.fi/tjko/projects.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jpegoptim can optimize and compress jpeg files. Program supports
lossless optimization, which is based on optimizing the Huffman
tables. So called, "lossy" optimization (compression) is done by
re-encoding the image using user specified image quality factor.

%description -l pl.UTF-8
Jpegoptim potrafi optymalizować i kompresować pliki jpeg. Program
dokonuje bezstratnej optymalizacji opartej na optymalizacji tablic
Huffmana. Optymalizacja stratna (kompresja) jest dokonywana przez
przekodowanie obrazu z podaną przez użytkownika jakością.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub aux
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*