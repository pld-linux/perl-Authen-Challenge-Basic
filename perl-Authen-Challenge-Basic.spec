%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Authen-Challenge-Basic perl module
Summary(pl):	Modu� perla Authen-Challenge-Basic
Name:		perl-Authen-Challenge-Basic
Version:	0.1
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Authen::Challenge/Authen-Challenge-Basic-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-Digest-MD5
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Authen-Challenge-Basic authentication module

%description -l pl
Modu� autentykacji Authen-Challenge-Basic

%prep
%setup -q -n Authen-Challenge-Basic-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Authen/Challenge/Basic
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%dir %{perl_sitelib}/Authen/Challenge
%{perl_sitelib}/Authen/Challenge/Basic.pm

%dir %{perl_sitearch}/auto/Authen/Challenge
%{perl_sitearch}/auto/Authen/Challenge/Basic

%{_mandir}/man3/*
