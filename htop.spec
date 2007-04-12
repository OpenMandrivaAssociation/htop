Summary:	Interactive text-mode process viewer for Linux
Name:		htop
Version:	0.6.5
Release: 	%mkrel 1
Source0:	http://prdownloads.sourceforge.net/htop/%{name}-%{version}.tar.bz2
License:	GPL
Group:		Monitoring
Url:		http://htop.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: ncurses-devel
BuildRequires: desktop-file-utils

%description
htop is an interactive process viewer for Linux, similar to top.
It requires ncurses. Tested with Linux 2.4 and 2.6.
Some advantages over top :
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
rm -rf $RPM_BUILD_ROOT
%makeinstall

mkdir -p %buildroot/%_menudir

cat > $RPM_BUILD_ROOT%{_menudir}/%{name} << EOF
?package(%name): needs="terminal" \
        section="System/Monitoring" \
        title="%{name}" \
        longtitle="%{summary}" \
        command="%{_bindir}/%{name}" \
        icon="%{name}.png" \
        xdg="true"
EOF

desktop-file-install --vendor="" \
  --add-category="System" \
  --add-category="Monitor" \
  --add-category="X-MandrivaLinux-System-Monitoring" \
  --remove-category="Application" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README AUTHORS NEWS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_menudir}/%name
%{_mandir}/man1/%{name}.*



