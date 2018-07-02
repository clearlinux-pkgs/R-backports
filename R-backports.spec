#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-backports
Version  : 1.1.2
Release  : 27
URL      : https://cran.r-project.org/src/contrib/backports_1.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/backports_1.1.2.tar.gz
Summary  : Reimplementations of Functions Introduced Since R-3.0.0
Group    : Development/Tools
License  : GPL-2.0
Requires: R-backports-lib
BuildRequires : clr-R-helpers

%description
R since version 3.0.0. The backports are conditionally exported which
    results in R resolving the function names to the version shipped with R (if
    available) and uses the implemented backports as fallback. This way package
    developers can make use of the new functions without worrying about the
    minimum required R version.

%package lib
Summary: lib components for the R-backports package.
Group: Libraries

%description lib
lib components for the R-backports package.


%prep
%setup -q -c -n backports

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523288669

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523288669
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library backports
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library backports
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library backports
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library backports|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/backports/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/backports/libs/backports.so
/usr/lib64/R/library/backports/libs/backports.so.avx2
/usr/lib64/R/library/backports/libs/backports.so.avx512
