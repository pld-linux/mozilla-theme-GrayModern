Summary:	Like Modern, only gray
Summary(pl):	Identyczny jak Modern, tylko ¿e szary
Name:		mozilla-theme-GrayModern
Version:	1.0.2
%define		_realname	graymodern
%define		_snap		%{version}_1.0-RC3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.us-east1.mozdev.org/themes/%{_realname}_%{_snap}.jar
# Source0-md5:	8ab4f2abb0046d66525b7659f5a18eb0
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/skins/graymodern.html
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

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
