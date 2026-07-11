%global tl_name endiagram
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1d
Release:	%{tl_revision}.1
Summary:	Easy creation of potential energy curve diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/endiagram
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/endiagram.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/endiagram.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the facility of drawing potential energy curve
diagrams with just a few simple commands. The package cannot (yet) be
considered stable.

