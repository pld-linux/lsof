Summary:	Lists files open by processes
Summary(pl):	Program do ¶ledzenia wszystkich procesów w systemie
Name:		lsof
Version:	4.43
Release:	1
Copyright:	Free
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Vendor:		Vic Abell <abe@purdue.edu>
URL:		ftp://vic.cc.purdue.edu/pub/tools/unix/lsof
Source:		%{name}_%{version}_W.tar.gz
Buildroot:	/tmp/%{name}-%{version}-root

%description
Lsof's name stands for LiSt Open Files, and it does just that. It lists
information about files that are open by the processes running on a UNIX
system.

%description -l pl
Lsof (LiSt Open Files) ¶ledzi wszystkie procesy jakie s± w danej chwili
uruchomine w systemie. Program ten jest bardzo pomocnym narzêdziem dla
administratora systemu Unix.

%prep
%setup -c -n %{name}
tar xvf %{name}_%{version}.tar

%build
rm -rf $RPM_BUILD_ROOT
cd %{name}_%{version}

./Configure -n linux
make DEBUG="$RPM_OPT_FLAGS"

%clean
rm -rf $RPM_BUILD_ROOT

%install
cd %{name}_%{version}

install -d $RPM_BUILD_ROOT%{_prefix}/{sbin,share/man/man8}

install -s lsof $RPM_BUILD_ROOT%{_sbindir}
install lsof.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man8/* 00*

%files
%defattr(644,root,root,755)
%doc %{name}_%{version}/00*

%attr(755,root,root) %{_sbindir}/lsof
%{_mandir}/man8/*

%changelog
* Sun Sep 27 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [4.37-1d]
- updated to 4.37,
- build against PLD Tornado,
- translation modified for pl,
- build from root account -> needed to build /proc-based lsof
- restricted files permissions,
- macro %%{name} in Patch.

* Mon Jun 29 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
  [4.34-1]
- New version
- Spec rewriten to use %{name} and %{version} macros
- Removed old log enteries
