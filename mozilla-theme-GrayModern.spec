Summary:	Like Modern, only gray
Summary(pl):	Identyczny jak Modern, tylko ¿e szary
Name:		mozilla-theme-GrayModern
%define		_realversion 2003-08-28
Version:	%(echo %{_realversion}|tr -d - )
%define		_realname	graymodern
%define		_mozdestrel	1.5b
%define		_snap		%{_realversion}_%{_mozdestrel}
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/themes/%{_realname}_%{_snap}.jar
# Source0-md5:	a29d1da4482d2315123e495fdaf5efdb
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/themes/graymodern.html
Requires(post,postun):	textutils
Requires:	mozilla = 5:1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Like Modern, only gray.

%description -l pl
Identyczny jak Modern, tylko ¿e szary.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
