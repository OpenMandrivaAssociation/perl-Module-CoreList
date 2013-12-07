%define modname Module-CoreList
%define modver 2.91

Summary:	Tell what modules shipped with versions of perl
Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Module/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Module::CoreList contains data about what perl modules are shipped
with given versions of perl (and their versions). It comes also with a
command-line utility, corelist, to retrieve this information easily.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/corelist
%{perl_vendorlib}/Module
%{_mandir}/man1/*
%{_mandir}/man3/*

