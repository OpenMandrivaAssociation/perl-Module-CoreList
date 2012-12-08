%define upstream_name	 Module-CoreList
%define upstream_version 2.59

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Tell what modules shipped with versions of perl
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Module::CoreList contains data about what perl modules are shipped
with given versions of perl (and their versions). It comes also with a
command-line utility, corelist, to retrieve this information easily.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Module
%{_mandir}/*/*
%{_bindir}/corelist



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.590.0-4
+ Revision: 765487
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.590.0-3
+ Revision: 763982
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 2.590.0-2
+ Revision: 763092
- rebuild

* Tue Jan 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.590.0-1
+ Revision: 759438
- version update 2.59

* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.530.0-1
+ Revision: 690289
- update to new version 2.53

* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.520.0-1
+ Revision: 688752
- update to new version 2.52

* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.510.0-1
+ Revision: 686641
- update to new version 2.51

* Sun May 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.490.0-1
+ Revision: 674806
- update to new version 2.49

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.460.0-2
+ Revision: 667259
- mass rebuild

* Wed Mar 23 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.460.0-1
+ Revision: 648089
- update to new version 2.46

* Thu Feb 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.450.0-1
+ Revision: 639657
- update to new version 2.45

* Tue Feb 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.440.0-1
+ Revision: 634701
- update to new version 2.44

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.420.0-1mdv2011.0
+ Revision: 625275
- update to new version 2.42

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.410.0-1mdv2011.0
+ Revision: 601902
- update to new version 2.41
- update to new version 2.40

* Mon Aug 23 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.370.0-1mdv2011.0
+ Revision: 572223
- update to 2.37

* Tue Jul 27 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.360.0-1mdv2011.0
+ Revision: 561032
- update to 2.36

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.350.0-1mdv2011.0
+ Revision: 552413
- update to 2.35

* Wed Apr 21 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.310.0-1mdv2010.1
+ Revision: 537576
- update to 2.31

* Sun Apr 18 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.290.0-1mdv2010.1
+ Revision: 536190
- update to 2.29

* Tue Feb 23 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.260.0-1mdv2010.1
+ Revision: 510079
- update to 2.26

* Thu Jan 21 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.250.0-1mdv2010.1
+ Revision: 494443
- update to 2.25

* Mon Dec 21 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.240.0-1mdv2010.1
+ Revision: 480729
- update to 2.24

* Sat Nov 21 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.230.0-1mdv2010.1
+ Revision: 467870
- update to 2.23

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.220.0-1mdv2010.1
+ Revision: 460763
- update to 2.22

* Tue Aug 25 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.180.0-1mdv2010.0
+ Revision: 420890
- update to 2.18

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.170.0-1mdv2010.0
+ Revision: 401632
- rebuild using %%perl_convert_version
- fixed license field

* Mon Jan 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.17-1mdv2009.1
+ Revision: 331147
- update to new version 2.17

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.15-2mdv2009.0
+ Revision: 268616
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.15-1mdv2009.0
+ Revision: 193863
- update to new version 2.15

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Dec 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.13-1mdv2008.1
+ Revision: 135967
- update to new version 2.13

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.12-1mdv2008.0
+ Revision: 52504
- update to new version 2.12

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.11-1mdv2008.0
+ Revision: 46652
- update to new version 2.11

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 2.09-1mdv2008.0
+ Revision: 20280
- 2.09


* Fri Aug 11 2006 rafael
+ 08/11/06 10:25:06 (55603)
2.07

* Mon Aug 07 2006 rafael
+ 08/07/06 15:45:38 (53985)
2.06

* Mon Aug 07 2006 rafael
+ 08/07/06 15:44:39 (53984)
Import perl-Module-CoreList

* Thu Jun 08 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.05-1mdv2007.0
- New release 2.05
- fix directory ownerhsip
- HTTP source URL
- spec cleanup

* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.04-2mdk
- Fix According to perl Policy
	- Source URL

* Thu Feb 02 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.04-1mdk
- 2.04

* Wed Feb 01 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.03-1mdk
- 2.03

* Tue May 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.02-1mdk
- 2.02

* Mon Apr 25 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.01-1mdk
- 2.01

* Fri Apr 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.00-1mdk
- 2.00
- Drop patch 0 (now that this module is part of the perl core)

* Wed Jan 05 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.98-1mdk
- New version

* Wed Dec 01 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.97-1mdk
- Initial MDK release.

