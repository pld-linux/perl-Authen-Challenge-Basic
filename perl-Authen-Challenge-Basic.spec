%include	/usr/lib/rpm/macros.perl
Summary:	Authen-Challenge-Basic perl module
Summary(pl):	Modu³ perla Authen-Challenge-Basic
Name:		perl-Authen-Challenge-Basic
Version:	0.1
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Authen::Challenge/Authen-Challenge-Basic-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Digest-MD5
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen-Challenge-Basic authentication module.

%description -l pl
Modu³ autentykacji Authen-Challenge-Basic.

%prep
%setup -q -n Authen-Challenge-Basic-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
