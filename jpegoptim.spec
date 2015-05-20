Summary:	Utility for optimizing and compressing JPEG files
Summary(pl.UTF-8):	Program do optymalizacji i kompresji plików JPEG.
Name:		jpegoptim
Version:	1.4.3
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://www.kokkonen.net/tjko/src/%{name}-%{version}.tar.gz
# Source0-md5:	52987700d1db3a3002ec32b1d0dac489
URL:		http://www.kokkonen.net/tjko/projects.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel >= 6
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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README
%attr(755,root,root) %{_bindir}/jpegoptim
%{_mandir}/man1/jpegoptim.1*
