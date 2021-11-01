Summary:	Lists files open by processes
Summary(es.UTF-8):	Lista los archivos abiertos por los procesos que están en ejecución
Summary(pl.UTF-8):	Program do śledzenia wszystkich procesów w systemie
Summary(pt_BR.UTF-8):	Lista os arquivos abertos pelos processos que estão rodando
Summary(ru.UTF-8):	Показывает открытые процессами файлы
Summary(uk.UTF-8):	Показує відкриті процесами файли
Name:		lsof
Version:	4.94.0
Release:	1
License:	Free
Group:		Applications/System
Source0:	https://github.com/lsof-org/lsof/releases/download/%{version}/lsof_%{version}.linux.tar.bz2
# Source0-md5:	2a007f86fb0207fbce3e9d7542e1041c
URL:		http://people.freebsd.org/~abe/
BuildRequires:	libselinux-devel
BuildRequires:	libtirpc-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lsof's name stands for LiSt Open Files, and it does just that. It
lists information about files that are open by the processes running
on a UNIX system.

%description -l es.UTF-8
El nombre lsof significa LiSt Open Files, y lo que hace es: lista los
archivos abiertos. Hace una relación, con información variada, sobre
los archivos abiertos por los procesos en ejecución en un sistema
UNIX.

%description -l pl.UTF-8
Lsof (LiSt Open Files) śledzi wszystkie procesy jakie są w danej
chwili uruchomione w systemie. Program ten jest bardzo pomocnym
narzędziem dla administratora systemu Unix.

%description -l pt_BR.UTF-8
O nome lsof significa LiSt Open Files, e faz isto: lista os arquivos
abertos. Ele lista várias informações sobre os arquivos abertos pelos
processos que estão rodando em um sistema UNIX.

%description -l ru.UTF-8
Lsof - это сокращение от LiSt Open Files. Именно это программа lsof и
делает - выводит информацию о файлах, открытых процессами, работающими
в системе.

%description -l uk.UTF-8
Lsof - це скорочення від LiSt Open Files. Саме це програма lsof і
робить - виводить інформацію про файли, відкриті працюючими процесами.

%prep
%setup -q -n %{name}_%{version}.linux

%build
LSOF_CC="%{__cc}"; export LSOF_CC
./Configure -n linux
%{__make} \
	DEBUG="%{rpmcppflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install lsof $RPM_BUILD_ROOT%{_bindir}
install lsof.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {00*,README.*}
%attr(755,root,root) %{_bindir}/lsof
%{_mandir}/man8/lsof.8*
