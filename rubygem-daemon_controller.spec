# Generated from daemon_controller-0.2.6.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	daemon_controller

Summary:	A library for implementing daemon management capabilities
Name:		rubygem-%{rbname}

Version:	0.2.6
Release:	1
Group:		Development/Ruby
License:	BSD
URL:		http://github.com/FooBarWidget/daemon_controller/tree/master
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
A library for robust daemon management.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f spec/

%install
%gem_install

%files
%doc LICENSE.txt README.markdown
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/daemon_controller
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/daemon_controller/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}



%changelog
* Tue Mar 29 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.2.6-1
+ Revision: 648727
- imported package rubygem-daemon_controller


* Tue Mar 29 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.2.6-1
- Initial package
