%include	/usr/lib/rpm/macros.perl
Summary:	Authen-Challenge-Basic perl module
Summary(pl):	Modu³ perla Authen-Challenge-Basic
Name:		perl-Authen-Challenge-Basic
Version:	0.1
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Authen::Challenge/Authen-Challenge-Basic-%{version}.tar.gz
Patch0:		%{name}-Digest-MD5.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen-Challenge-Basic authentication module.

%description -l pl
Modu³ autentykacji Authen-Challenge-Basic.

%prep
%setup -q -n Authen-Challenge-Basic-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{perl_sitelib}/Authen/Challenge
%{perl_sitelib}/Authen/Challenge/Basic.pm
%{_mandir}/man3/*
