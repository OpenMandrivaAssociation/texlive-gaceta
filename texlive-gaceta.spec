# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/gaceta
# catalog-date 2008-08-19 21:00:04 +0200
# catalog-license lppl
# catalog-version 1.06
Name:		texlive-gaceta
Version:	1.06
Release:	9
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

%description
The class will typeset papers for <<La Gaceta de la Real
Sociedad Matematica Espanola>>.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gaceta/gaceta.cls
%doc %{_texmfdistdir}/doc/latex/gaceta/README
%doc %{_texmfdistdir}/doc/latex/gaceta/plantilla-articulo-de-seccion.pdf
%doc %{_texmfdistdir}/doc/latex/gaceta/plantilla-articulo-de-seccion.tex
%doc %{_texmfdistdir}/doc/latex/gaceta/plantilla-articulo-suelto.pdf
%doc %{_texmfdistdir}/doc/latex/gaceta/plantilla-articulo-suelto.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.06-2
+ Revision: 752179
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.06-1
+ Revision: 718517
- texlive-gaceta
- texlive-gaceta
- texlive-gaceta
- texlive-gaceta

