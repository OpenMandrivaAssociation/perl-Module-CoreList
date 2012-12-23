%define upstream_name	 Module-CoreList
%define upstream_version 2.79

Summary:	Tell what modules shipped with versions of perl
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Module::CoreList contains data about what perl modules are shipped
with given versions of perl (and their versions). It comes also with a
command-line utility, corelist, to retrieve this information easily.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

# MD 20121223 conflcits with perl 5.16
rm -f %{buildroot}/%{_mandir}/man1/corelist.1*

%files
%doc Changes README
%{perl_vendorlib}/Module
%{_mandir}/*/*
%{_bindir}/corelist

