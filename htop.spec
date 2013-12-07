Summary:        Interactive text-mode process viewer for Linux
Name:           htop
Version:        1.0.2
Release:        4
License:        GPLv2+
Group:          Monitoring
Url:            http://htop.sourceforge.net/
Source0:        http://ovh.dl.sourceforge.net/htop/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(ncurses++w)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(menuw)
BuildRequires:  pkgconfig(formw)

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
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std
# A hack to hide htop.from the menu
rm -f %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc README AUTHORS NEWS
%{_bindir}/%{name}
%{_datadir}/pixmaps/*
%{_mandir}/man1/%{name}.*

