Summary:	Lists files open by processes
Summary(pl):	Program do ¶ledzenia wszystkich procesów w systemie
Name:		lsof
Version:	4.60
Release:	1
License:	Free
Group:		Applications/System
Vendor:		Vic Abell <abe@purdue.edu>
Source0:	ftp://vic.cc.purdue.edu/pub/tools/unix/lsof/%{name}_%{version}_W.tar.gz
Patch0:		%{name}-linux-ipv6mapped.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lsof's name stands for LiSt Open Files, and it does just that. It
lists information about files that are open by the processes running
on a UNIX system.

%description -l pl
Lsof (LiSt Open Files) ¶ledzi wszystkie procesy jakie s± w danej
chwili uruchomine w systemie. Program ten jest bardzo pomocnym
narzêdziem dla administratora systemu Unix.

%prep
%setup -c -q -n %{name}
tar xf %{name}_%{version}.tar
#%patch -p1

%build
cd %{name}_%{version}

./Configure -n linux
%{__make} DEBUG="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

cd %{name}_%{version}

install lsof $RPM_BUILD_ROOT%{_sbindir}
install lsof.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf 00*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}_%{version}/00*

%attr(755,root,root) %{_sbindir}/lsof
%{_mandir}/man8/*
