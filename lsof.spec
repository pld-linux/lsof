Summary:	Lists files open by processes
Summary(pl):	Program do ¶ledzenia wszystkich procesów w systemie
Name:		lsof
Version:	4.45
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
%setup -c -q -n %{name}
tar xf %{name}_%{version}.tar

%build
cd %{name}_%{version}

./Configure -n linux
make DEBUG="$RPM_OPT_FLAGS"

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

cd %{name}_%{version}

install -d	$RPM_BUILD_ROOT%{_prefix}/{sbin,share/man/man8}

install -s lsof	$RPM_BUILD_ROOT%{_sbindir}
install lsof.8	$RPM_BUILD_ROOT%{_mandir}/man8

gzip -9fn	$RPM_BUILD_ROOT%{_mandir}/man8/* 00*

%files
%defattr(644,root,root,755)
%doc %{name}_%{version}/00*

%attr(755,root,root) %{_sbindir}/lsof
%{_mandir}/man8/*
