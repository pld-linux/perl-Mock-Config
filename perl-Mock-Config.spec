#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Mock
%define		pnam	Config
%include	/usr/lib/rpm/macros.perl
Summary:	Mock::Config - temporarily set Config or XSConfig values
Summary(pl.UTF-8):	Mock::Config - tymczasowe ustawianie wartości Config lub XSConfig
Name:		perl-Mock-Config
Version:	0.03
Release:	1
License:	Artistic v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RU/RURBAN/Mock-Config-%{version}.tar.gz
# Source0-md5:	27d250fb893974ba713d0d9c8e730729
URL:		http://search.cpan.org/dist/Mock-Config/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
