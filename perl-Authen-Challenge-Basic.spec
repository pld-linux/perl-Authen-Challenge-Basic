%include	/usr/lib/rpm/macros.perl
Summary:	Authen::Challenge::Basic perl module
Summary(pl):	Modu³ perla Authen::Challenge::Basic
Name:		perl-Authen-Challenge-Basic
Version:	0.1
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Authen/Authen-Challenge-Basic-%{version}.tar.gz
Patch0:		%{name}-Digest-MD5.patch
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::Challenge::Basic authentication module.

%description -l pl
Modu³ autentykacji Authen::Challenge::Basic.

%prep
%setup -q -n Authen-Challenge-Basic-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_sitelib}/Authen/Challenge
%{perl_sitelib}/Authen/Challenge/Basic.pm
%{_mandir}/man3/*
