# revision 30025
# category Package
# catalog-ctan /macros/latex/contrib/endiagram
# catalog-date 2013-04-05 11:53:55 +0200
# catalog-license lppl1.3
# catalog-version 0.1b
Name:		texlive-endiagram
Version:	0.1b
Release:	1
Summary:	Easy creation of potential energy curve diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/endiagram
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endiagram.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endiagram.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the facility of drawing potential energy
curve diagrams with just a few simple commands. The package
cannot (yet) be considered stable.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/endiagram/endiagram.sty
%doc %{_texmfdistdir}/doc/latex/endiagram/README
%doc %{_texmfdistdir}/doc/latex/endiagram/endiagram_en.pdf
%doc %{_texmfdistdir}/doc/latex/endiagram/endiagram_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
