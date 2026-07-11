%global tl_name gaceta
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.06
Release:	%{tl_revision}.1
Summary:	A class to typeset La Gaceta de la RSME
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gaceta
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gaceta.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gaceta.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class will typeset papers for <<La Gaceta de la Real Sociedad
Matematica Espanola>>.

