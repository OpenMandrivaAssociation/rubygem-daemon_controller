# Generated from daemon_controller-0.2.6.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	daemon_controller

Summary:	A library for implementing daemon management capabilities
Name:		rubygem-%{rbname}

Version:	1.2.0
Release:	3
Group:		Development/Ruby
License:	BSD
URL:		https://github.com/FooBarWidget/daemon_controller/tree/master
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
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/daemon_controller
%{gem_dir}/gems/%{rbname}-%{version}/lib/daemon_controller/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/spec
%{gem_dir}/gems/%{rbname}-%{version}/spec/*
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{gem_dir}/doc/%{rbname}-%{version}

