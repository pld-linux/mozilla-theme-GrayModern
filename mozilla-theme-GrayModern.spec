Summary:	Like Modern, only gray
Summary(pl):	Identyczny jak Modern, tylko ¿e szary
Name:		mozilla-theme-GrayModern
Version:	1.0.3
%define		_realname	graymodern
%define		_mozrel		1.2.1
%define		_snap		%{version}_%{_mozrel}
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.us-east3.mozdev.org/themes/themes/%{_realname}_%{_snap}.jar
# Source0-md5:	81f2801a0ac9a0ecc215b5d9e7b28bc3
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/themes/graymodern.html
Requires(post,postun):	textutils
Requires:	mozilla >= %{_mozrel}
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
