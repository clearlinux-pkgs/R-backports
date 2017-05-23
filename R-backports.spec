#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-backports
Version  : 1.1.0
Release  : 5
URL      : https://cran.r-project.org/src/contrib/backports_1.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/backports_1.1.0.tar.gz
Summary  : Reimplementations of Functions Introduced Since R-3.0.0
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n backports

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1495516719

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1495516719
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library backports
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library backports


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/backports/DESCRIPTION
/usr/lib64/R/library/backports/INDEX
/usr/lib64/R/library/backports/Meta/Rd.rds
/usr/lib64/R/library/backports/Meta/features.rds
/usr/lib64/R/library/backports/Meta/hsearch.rds
/usr/lib64/R/library/backports/Meta/links.rds
/usr/lib64/R/library/backports/Meta/nsInfo.rds
/usr/lib64/R/library/backports/Meta/package.rds
/usr/lib64/R/library/backports/NAMESPACE
/usr/lib64/R/library/backports/NEWS.md
/usr/lib64/R/library/backports/R/backports
/usr/lib64/R/library/backports/R/backports.rdb
/usr/lib64/R/library/backports/R/backports.rdx
/usr/lib64/R/library/backports/help/AnIndex
/usr/lib64/R/library/backports/help/aliases.rds
/usr/lib64/R/library/backports/help/backports.rdb
/usr/lib64/R/library/backports/help/backports.rdx
/usr/lib64/R/library/backports/help/paths.rds
/usr/lib64/R/library/backports/html/00Index.html
/usr/lib64/R/library/backports/html/R.css
