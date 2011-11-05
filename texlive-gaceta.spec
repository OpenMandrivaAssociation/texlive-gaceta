# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/gaceta
# catalog-date 2008-08-19 21:00:04 +0200
# catalog-license lppl
# catalog-version 1.06
Name:		texlive-gaceta
Version:	1.06
Release:	1
Summary:	A class to typeset La Gaceta de la RSME
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gaceta
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gaceta.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gaceta.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The class will typeset papers for <<La Gaceta de la Real
Sociedad Matematica Espanola>>.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gaceta/gaceta.cls
%doc %{_texmfdistdir}/doc/latex/gaceta/README
%doc %{_texmfdistdir}/doc/latex/gaceta/plantilla-articulo-de-seccion.pdf
%doc %{_texmfdistdir}/doc/latex/gaceta/plantilla-articulo-de-seccion.tex
%doc %{_texmfdistdir}/doc/latex/gaceta/plantilla-articulo-suelto.pdf
%doc %{_texmfdistdir}/doc/latex/gaceta/plantilla-articulo-suelto.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
