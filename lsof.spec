Summary:	Lists files open by processes
Summary(es):	Lista los archivos abiertos por los procesos que estАn en ejecuciСn
Summary(pl):	Program do ╤ledzenia wszystkich procesСw w systemie
Summary(pt_BR):	Lista os arquivos abertos pelos processos que estЦo rodando
Summary(ru):	Показывает открытые процессами файлы
Summary(uk):	Показу╓ в╕дкрит╕ процесами файли
Name:		lsof
Version:	4.60
Release:	2
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

%description -l es
El nombre lsof significa LiSt Open Files, y lo que hace es: lista los
archivos abiertos. Hace una relaciСn, con informaciСn variada, sobre
los archivos abiertos por los procesos en ejecuciСn en un sistema
UNIX.

%description -l pl
Lsof (LiSt Open Files) ╤ledzi wszystkie procesy jakie s╠ w danej
chwili uruchomine w systemie. Program ten jest bardzo pomocnym
narzЙdziem dla administratora systemu Unix.

%description -l pt_BR
O nome lsof significa LiSt Open Files, e faz isto: lista os arquivos
abertos. Ele lista vАrias informaГУes sobre os arquivos abertos pelos
processos que estЦo rodando em um sistema UNIX.

%description -l ru
Lsof - это сокращение от LiSt Open Files. Именно это программа lsof и
делает - выводит информацию о файлах, открытых процессами, работающими
в системе.

%description -l uk
Lsof - це скорочення в╕д LiSt Open Files. Саме це програма lsof ╕
робить - виводить ╕нформац╕ю про файли, в╕дкрит╕ працюючими процесами.

%prep
%setup -c -q -n %{name}
tar xf %{name}_%{version}.tar
#%patch -p1

%build
cd %{name}_%{version}

./Configure -n linux
%{__make} \
	LSOF_CC="%{__cc}" \
	DEBUG="%{rpmcflags}"

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
