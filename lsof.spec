Summary:	Lists files open by processes
Summary(es):	Lista los archivos abiertos por los procesos que estАn en ejecuciСn
Summary(pl):	Program do ╤ledzenia wszystkich procesСw w systemie
Summary(pt_BR):	Lista os arquivos abertos pelos processos que estЦo rodando
Summary(ru):	Показывает открытые процессами файлы
Summary(uk):	Показу╓ в╕дкрит╕ процесами файли
Name:		lsof
Version:	4.72
Release:	1
License:	Free
Vendor:		Vic Abell <abe@purdue.edu>
Group:		Applications/System
Source0:	ftp://vic.cc.purdue.edu/pub/tools/unix/lsof/%{name}_%{version}.tar.bz2
# Source0-md5:	5cc6edeab12733c69bac8ed4246e25f2
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
%setup -c -q
cd %{name}_%{version}
tar xf %{name}_%{version}_src.tar

%build
cd %{name}_%{version}/%{name}_%{version}_src

LSOF_CC="%{__cc}"; export LSOF_CC
./Configure -n linux
%{__make} \
	DEBUG="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

cd %{name}_%{version}/%{name}_%{version}_src

install lsof $RPM_BUILD_ROOT%{_sbindir}
install lsof.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}_%{version}/{00*,README.*,RELEASE*} %{name}_%{version}/%{name}_%{version}_src/00*
%attr(755,root,root) %{_sbindir}/lsof
%{_mandir}/man8/*
