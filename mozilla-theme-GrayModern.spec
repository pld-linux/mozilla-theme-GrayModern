Summary:	Theme like Modern, only gray
Summary(pl.UTF-8):	Motyw identyczny jak Modern, tylko że szary
Name:		mozilla-theme-GrayModern
%define		_realname	graymodern
Version:	2004.09.15
%define		_snap		2004-09-15_1.7
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://mozilla-themes.schellen.net/%{_realname}_%{_snap}.jar
# Source0-md5:	688d397dbbd308813c338471f13eb342
Source1:	%{_realname}-installed-chrome.txt
URL:		http://mozilla-themes.schellen.net/
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 5:1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
Theme for Mozilla, like Modern only gray.

%description -l pl.UTF-8
Motyw dla Mozilli, identyczny jak Modern, tylko że szary.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
