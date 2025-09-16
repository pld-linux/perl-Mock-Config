#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Mock
%define		pnam	Config
Summary:	Mock::Config - temporarily set Config or XSConfig values
Summary(pl.UTF-8):	Mock::Config - tymczasowe ustawianie wartości Config lub XSConfig
Name:		perl-Mock-Config
Version:	0.05
Release:	1
License:	Artistic v2
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/R/RU/RURBAN/Mock-Config-%{version}.tar.gz
# Source0-md5:	4880e65bd309439a625d678b7d82ff97
URL:		https://metacpan.org/dist/Mock-Config
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mock::Config allows to temporarily set Config or XSConfig values.

%description -l pl.UTF-8
Mock::Config pozwala na tymczasowe ustawianie wartości Config lub
XSConfig.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Mock
%{perl_vendorlib}/Mock/Config.pm
%{_mandir}/man3/Mock::Config.3pm*
