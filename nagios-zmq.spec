Summary:	Nagios Event Broker to push Service,Host and Notifications events to Zeromq
Name:		nagios-zmq
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	https://github.com/mariussturm/nagios-zmq/tarball/master/%{name}.tgz
# Source0-md5:	43c6999a63067ee55bf7c13587518c58
URL:		https://github.com/mariussturm/nagios-zmq
BuildRequires:	json-c-devel
BuildRequires:	libuuid-devel
BuildRequires:	zeromq-devel < 3
Requires:	nagios
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		brokerdir	%{_libdir}/nagios/brokers

%description
nagios-zmq is a nagios event broker module that provides nagios
information on a zeromq publish/subscribe socket.

This allows you to get the check/notification on a 0mq without polling
Nagios all the time.

%prep
%setup -qc
mv mariussturm-nagios-zmq-60fc6ae/* .

%{__sed} -i -e 's/gcc/$(CC) $(OPTFLAGS) $(LDFLAGS)/' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{brokerdir}
install -p nagios-zmq.o $RPM_BUILD_ROOT%{brokerdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{brokerdir}/nagios-zmq.o
