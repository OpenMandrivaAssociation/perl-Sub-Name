%define modname	Sub-Name
%define modver 0.12

Summary:	Allows to (re)name a sub
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Sub/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildRequires: perl(Devel::CheckBin)

%description 
This module allows to (re)name a sub.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
%make test

%files
%doc Changes README
%{perl_vendorarch}/Sub
%{perl_vendorarch}/auto/Sub
%{_mandir}/man3/*
