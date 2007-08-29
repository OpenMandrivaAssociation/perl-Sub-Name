%define module  Sub-Name
%define	name	perl-%{module}
%define version 0.02
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Allows to (re)name a sub
License: 	GPL or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Sub/%{module}-%{version}.tar.gz
BuildRequires:  perl-devel
BuildRoot: 	    %{_tmppath}/%{name}-%{version}

%description 
This module allows to (re)name a sub.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%check
%{__make} test

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/Sub
%{perl_vendorarch}/auto/Sub
%{_mandir}/*/*

