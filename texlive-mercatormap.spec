Name:		texlive-mercatormap
Version:	56060
Release:	2
Summary:	Spherical Mercator coordinate systems and Web Mercator tile integration
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mercatormap
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mercatormap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mercatormap.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package extends TikZ with tools to create map graphics.
The provided coordinate system relies on the Web Mercator
projection used on the Web by OpenStreetMap and others. The
package supports the seamless integration of graphics from
public map tile servers by a Python script. Also, common map
elements like markers, geodetic networks, bar scales, routes,
orthodrome pieces, and more are part of the package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/mercatormap
%doc %{_texmfdistdir}/doc/latex/mercatormap

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
