%define module	Kwiki
%define name	perl-%{module}
%define version 0.39
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	The Kwiki Wiki Building Framework 
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
License:	GPL
Group:		Development/Perl
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Spoon)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Kwiki is perhaps the simplest to install, most modular, and easiest to extend
Wiki. A Wiki allows users to freely create and edit web pages in any web
browser. Kwiki is Open Source Software in Perl, and is available on CPAN.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
#%make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Kwiki
%{perl_vendorlib}/Kwiki.pm
%{_mandir}/*/*
%{_bindir}/*


