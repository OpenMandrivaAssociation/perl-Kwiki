%define upstream_name	 Kwiki
%define upstream_version 0.39

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	The Kwiki Wiki Building Framework 
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Spoon)
BuildArch:	noarch

%description
Kwiki is perhaps the simplest to install, most modular, and easiest to extend
Wiki. A Wiki allows users to freely create and edit web pages in any web
browser. Kwiki is Open Source Software in Perl, and is available on CPAN.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
#%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Kwiki
%{perl_vendorlib}/Kwiki.pm
%{_mandir}/*/*
%{_bindir}/*


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.390.0-1mdv2010.0
+ Revision: 402566
- update to 0.56

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.39-4mdv2009.0
+ Revision: 257390
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.39-3mdv2009.0
+ Revision: 245412
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.39-1mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Mar 08 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.39-1mdv2007.1
+ Revision: 138514
- new version

* Fri Sep 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-3mdv2007.0
- Rebuild

* Tue Apr 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-2mdk
- Rebuild
- better sources URL
- better buildrequires syntax

* Tue Apr 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-1mdk 
- first mandriva release

