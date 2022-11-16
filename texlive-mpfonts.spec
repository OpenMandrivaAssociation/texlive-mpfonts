Name:		texlive-mpfonts
Version:	54512
Release:	1
Summary:	Computer Modern Type 3 fonts converted using MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mpfonts
License:	knuth lppl1.3c ofl other-free pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpfonts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpfonts.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Computer Modern fonts are available in Type 1 format, but
these renditions are somewhat thin and spindly, and produce
much lighter results than the originals. It is alternatively
possible to use Metafont bitmaps, but this has its
disadvantages in comparison with vector fonts. These fonts are
conversions to Type 3 fonts, done entirely in MetaPost; they
are vector fonts which are a direct conversion from the
original Metafont files, so they are the design most authentic
to the originals. However, these fonts, because they are
PostScript Type 3 fonts, are not suitable for on-screen
reading, and should probably only be used for printing. Note:
do NOT add the map file to updmap!

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/type3/mpfonts
%{_texmfdistdir}/fonts/map/dvips/mpfonts
%doc %{_texmfdistdir}/doc/fonts/mpfonts

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
