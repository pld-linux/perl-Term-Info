#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Term
%define	pnam	Info
Summary:	Term::Info - Perl wrapper for ncurses tput
Summary(pl):	Term::Info - Perlowa przej¶ciówka dla ncurses tput
Name:		perl-Term-Info
Version:	1.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a2725f773d13f37921a371604517088a
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov 
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a wrapper for tput command, that allows you to get
information about terminal control codes.

%description -l pl
Ten modu³ jest otoczk± dla wywo³ywania polecenia tput, która pozwala
uzyskaæ informacje o kodach steruj±cych terminala.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{perl_vendorlib}/Term/Info.pm
