Name:		texlive-endiagram
Version:	34486
Release:	2
Summary:	Easy creation of potential energy curve diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/endiagram
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endiagram.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endiagram.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
