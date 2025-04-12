%global octpkg packajoozle

# there are not official releases yet.
%global commit	d7cec7de54fe529bfd6adb2e584d6505e7e1ce4f

Summary:	Enhanced package manager for GNU Octave
Name:		octave-packajoozle
Version:	dev
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/packajoozle/
Url:		https://github.com/apjanke/octave-packajoozle/
Source0:	https://github.com/apjanke/octave-packajoozle/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  octave-devel >= 4.4.1

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Packajoozle is a re-working of Octave’s pkg package management tool to use OOP.
It provides the pkj command, a drop-in replacement for pkg.

It was started as just a fun exercise, but it kind of got out of hand, and now
it’s almost a real, usable package.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{commit}

# fix version inside DESCRIPTION
sed -i -e "s|Version: 0.0.0+|Version: %{version}|" DESCRIPTION

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

