Name:		texlive-gaceta
Version:	15878
Release:	1
Summary:	A class to typeset La Gaceta de la RSME
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gaceta
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gaceta.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gaceta.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
