%define modname	Sub-Name
%define modver	0.26

Summary:	Allows to (re)name a sub
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Sub::Name
Source0:	http://www.cpan.org/modules/by-module/Sub/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description 
This module allows to (re)name a sub.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%check
%make test

%files
%doc Changes README
%{perl_vendorarch}/Sub
%{perl_vendorarch}/auto/Sub
%{_mandir}/man3/*

