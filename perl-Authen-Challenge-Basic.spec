#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Authen::Challenge::Basic - a basic challenge/response authentication scheme
Summary(pl):	Authen::Challenge::Basic - podstawowy schemat uwierzytelniania wezwanie/odpowied�
Name:		perl-Authen-Challenge-Basic
Version:	0.1
Release:	9
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Authen/Authen-Challenge-Basic-%{version}.tar.gz
# Source0-md5:	baafb21abd63b3b8b7829ea082891a42
Patch0:		%{name}-Digest-MD5.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Digest-MD5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::Challenge::Basic Perl module provides a simple MD5-based
challenge/response protocol allowing for mutual peer authentication in
a session. The protocol includes timing information, so it is possible
to introduce time constraints in the session to help prevent attacks
that rely on adjusting the clock in one of the peers.

%description -l pl
Modu� Perla Authen::Challenge::Basic udost�pnia prosty, oparty o MD5,
protok� uwierzytelniania typu wezwanie/odpowied� umo�liwiaj�cy
wzajemne uwierzytelnianie partner�w podczas sesji. Protok� zawiera
informacje synchronizujace, wi�c mo�liwe jest wprowadzenie podczaes
sesji ogranicze� czasowych u�atwiaj�cych zapobieganie atakom opartym
na przestawieniu zegara jednego z partner�w.

%prep
%setup -q -n Authen-Challenge-Basic-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_vendorlib}/Authen/Challenge
%{perl_vendorlib}/Authen/Challenge/Basic.pm
%{_mandir}/man3/*
