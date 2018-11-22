#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Apache-Htpasswd
Version  : 1.9
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/K/KM/KMELTZ/Apache-Htpasswd-1.9.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KM/KMELTZ/Apache-Htpasswd-1.9.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libapache-htpasswd-perl/libapache-htpasswd-perl_1.9-1.debian.tar.xz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Apache-Htpasswd-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Apache::Htpasswd - Manage Unix crypt-style password file.
SYNOPSIS
use Apache::Htpasswd;

%package dev
Summary: dev components for the perl-Apache-Htpasswd package.
Group: Development
Provides: perl-Apache-Htpasswd-devel = %{version}-%{release}

%description dev
dev components for the perl-Apache-Htpasswd package.


%package license
Summary: license components for the perl-Apache-Htpasswd package.
Group: Default

%description license
license components for the perl-Apache-Htpasswd package.


%prep
%setup -q -n Apache-Htpasswd-1.9
cd ..
%setup -q -T -D -n Apache-Htpasswd-1.9 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Apache-Htpasswd-1.9/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Apache-Htpasswd
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Apache-Htpasswd/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Apache/Htpasswd.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Apache::Htpasswd.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Apache-Htpasswd/deblicense_copyright
