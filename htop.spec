%define _disable_rebuild_configure 1

Summary:	Interactive text-mode process viewer for Linux
Name:		htop
Version:	3.0.4
Release:	1
License:	GPLv2+
Group:		Monitoring
# Original but old sources
#Url:            http://htop.sourceforge.net/
#Source0:	https://github.com/hishamhm/htop/archive/%{version}.tar.gz
# Sources from fork which got the permission of the original creator of the project to continue it.
Url:		https://htop.dev
Source0:	https://github.com/htop-dev/htop/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(menuw)
BuildRequires:	pkgconfig(formw)

%description
htop is an interactive process viewer for Linux, similar to top.
It requires ncurses. Tested with Linux 2.4 and 2.6.

Some advantages over top:

* you can scroll the list vertically and horizontally to see
  all processes and complete command lines
* htop starts faster than top
* you don't need to type the process number to kill a process
* you don't need to type the process number or the priority value to
  renice a process
* htop supports mouse operation

%prep
%autosetup -p1
./autogen.sh

%build
%configure \
    --enable-taskstats \
    --enable-unicode \
    --enable-cgroup

%make_build

%install
%make_install
# A hack to hide htop.from the menu
rm -f %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc README AUTHORS NEWS
%{_bindir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/icons/*/*/*/*.*
%{_mandir}/man1/%{name}.*
