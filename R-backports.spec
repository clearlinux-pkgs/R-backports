#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-backports
Version  : 1.1.7
Release  : 50
URL      : https://cran.r-project.org/src/contrib/backports_1.1.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/backports_1.1.7.tar.gz
Summary  : Reimplementations of Functions Introduced Since R-3.0.0
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-backports-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
Functions introduced or changed since R v3.0.0 are re-implemented in this
    package. The backports are conditionally exported in order to let R resolve
    the function name to either the implemented backport, or the respective base
    version, if available. Package developers can make use of new functions or
    arguments by selectively importing specific backports to
    support older installations.

%package lib
Summary: lib components for the R-backports package.
Group: Libraries

%description lib
lib components for the R-backports package.


%prep
%setup -q -c -n backports
cd %{_builddir}/backports

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589508670

%install
export SOURCE_DATE_EPOCH=1589508670
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc backports || :


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
/usr/lib64/R/library/backports/tests/helper/helper.R
/usr/lib64/R/library/backports/tests/test_R_user_dir.R
/usr/lib64/R/library/backports/tests/test_URLencode.R
/usr/lib64/R/library/backports/tests/test_anyNA.R
/usr/lib64/R/library/backports/tests/test_capture.output.R
/usr/lib64/R/library/backports/tests/test_dQuote.R
/usr/lib64/R/library/backports/tests/test_deparse1.R
/usr/lib64/R/library/backports/tests/test_dir.exists.R
/usr/lib64/R/library/backports/tests/test_dotsElt.R
/usr/lib64/R/library/backports/tests/test_dotsLength.R
/usr/lib64/R/library/backports/tests/test_file.info.R
/usr/lib64/R/library/backports/tests/test_file.mode.R
/usr/lib64/R/library/backports/tests/test_file.mtime.R
/usr/lib64/R/library/backports/tests/test_file.size.R
/usr/lib64/R/library/backports/tests/test_get0.R
/usr/lib64/R/library/backports/tests/test_hasName.R
/usr/lib64/R/library/backports/tests/test_isFALSE.R
/usr/lib64/R/library/backports/tests/test_isTRUE.R
/usr/lib64/R/library/backports/tests/test_lengths.R
/usr/lib64/R/library/backports/tests/test_list2DF.R
/usr/lib64/R/library/backports/tests/test_startsWith.R
/usr/lib64/R/library/backports/tests/test_strrep.R
/usr/lib64/R/library/backports/tests/test_trimws.R
/usr/lib64/R/library/backports/tests/test_valid.factor.R
/usr/lib64/R/library/backports/tests/test_warningCondition.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/backports/libs/backports.so
