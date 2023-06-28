%undefine _debugsource_packages

%define modname	Sub-Name

Summary:	Allows to (re)name a sub
Name:		perl-%{modname}
Version:	0.27
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Sub::Name
Source0:	http://www.cpan.org/modules/by-module/Sub/%{modname}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description 
This module allows to (re)name a sub.

%prep
%autosetup -p1 -n %{modname}-%{version}

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

