Summary:	Utility for optimizing and compressing JPEG files.
Summary(pl):	Program do optymalizacji i kompresji plików JPEG.
Name:		jpegoptim
Version:	1.2.2
Release:	1
License:	GPL
Group:		Applications/Graphics
URL:		http://www.iki.fi/tjko/projects.html
Source0:	http://www.cc.jyu.fi/~tjko/src/%{name}-%{version}.tar.gz
# Source0-md5:	c7e92417badac7dcffab4245c113871c
BuildRequires:	autoconf
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jpegoptim can optimize and compress jpeg files. Program supports
lossless optimization, which is based on optimizing the Huffman
tables. So called, "lossy" optimization (compression) is done by
re-encoding the image using user specified image quality factor.

%description -l pl
Jpegoptim potrafi optymalizowaæ i kompresowaæ pliki jpeg. Program
dokonuje bezstratnej optymalizacji opartej na optymalizacji tablic
Huffmana. Optymalizacja stratna (kompresja) jest dokonywana przez
przekodowanie obrazu z podan± przez u¿ytkowika jako¶ci±.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%doc README
