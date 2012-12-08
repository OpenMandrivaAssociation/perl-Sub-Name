%define upstream_name    Sub-Name
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    5

Summary: 	Allows to (re)name a sub
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Sub/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildRoot: 	    %{_tmppath}/%{name}-%{version}-%{release}

%description 
This module allows to (re)name a sub.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-4mdv2012.0
+ Revision: 765664
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-3
+ Revision: 764175
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-2
+ Revision: 667317
- mass rebuild

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 596677
- update to 0.05

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 556151
- rebuild for perl 5.12

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 404421
- rebuild using %%perl_convert_version

* Sat Jul 19 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.0
+ Revision: 238726
- update to new version 0.04

* Thu Feb 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2008.1
+ Revision: 173562
- update to new version 0.03

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.02-2mdv2008.1
+ Revision: 152317
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Aug 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2008.0
+ Revision: 74276
- import perl-Sub-Name


* Wed Aug 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2008.0
- first mdv release
