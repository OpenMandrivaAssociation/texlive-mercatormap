%global tl_name mercatormap
%global tl_revision 79265

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.1
Release:	%{tl_revision}.1
Summary:	Spherical Mercator coordinate systems and Web Mercator tile integration
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mercatormap
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mercatormap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mercatormap.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package extends TikZ with tools to create map graphics. The
provided coordinate system relies on the Web Mercator projection used on
the Web by OpenStreetMap and others. The package supports the seamless
integration of graphics from public map tile servers by a Python script.
Also, common map elements like markers, geodetic networks, bar scales,
routes, orthodrome pieces, and more are part of the package.

