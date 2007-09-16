Name:           htop
Version:        0.6.6
Release:        %mkrel 2
Summary:        Interactive text-mode process viewer for Linux
License:        GPL
Group:          Monitoring
URL:            http://htop.sourceforge.net/
Source0:        http://ovh.dl.sourceforge.net/htop/htop-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%{configure2_5x}
%{make}

%install
rm -rf %{buildroot}
%{makeinstall}

desktop-file-install --vendor="" \
  --add-category="System" \
  --add-category="Monitor" \
  --remove-key="Path" \
  --remove-key="Version" \
  --remove-category="Application" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*


%clean
rm -rf %{buildroot}

%post
%{update_menus}
                
%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc README AUTHORS NEWS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_mandir}/man1/%{name}.*

