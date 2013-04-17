%global packname  psych
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.2.1
Release:          1
Summary:          Procedures for Psychological, Psychometric, and Personality Research
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-MASS R-GPArotation R-graph R-Rgraphviz R-mvtnorm
Requires:         R-polycor R-sem R-Rcsdp R-lavaan
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-MASS R-GPArotation R-graph R-Rgraphviz R-mvtnorm
BuildRequires:    R-polycor R-sem R-Rcsdp R-lavaan

%define debug_package %{nil}

%description
A number of routines for personality, psychometrics and experimental
psychology.  Functions are primarily for scale construction using factor
analysis, cluster analysis and reliability analysis, although others
provide basic descriptive statistics. Item Response Theory is done using
factor analysis of tetrachoric and polychoric correlations. Functions for
simulating particular item and test structures are included. Several
functions serve as a useful front end for structural equation modeling. 
Graphical displays of path diagrams, factor analysis and structural
equation models are created using basic graphics. Some of the functions
are written to support a book on psychometrics as well as publications in
personality research. For more information, see the
personality-project.org/r webpage.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
if [ x$DISPLAY != x ];	then %{_bindir}/R CMD check %{packname}
else			true
fi

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
