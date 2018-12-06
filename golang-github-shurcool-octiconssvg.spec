# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/octicon
%global commit          c42b0e3b24d96976ecac81ef691662777b39ef64
%global oldgoipath      github.com/shurcooL/octiconssvg
%global oldgoname       %gorpmname %{oldgoipath}

%global common_description %{expand:
Octicons provides GitHub Octicons in SVG format.}

%gometa

Name:           %{goname}ssvg
Version:        0
Release:        0.4%{?dist}
Summary:        GitHub Octicons in SVG format
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/net/html/atom)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%package -n compat-%{oldgoname}-devel
Summary:    %{summary}
BuildArch:  noarch

%description -n compat-%{oldgoname}-devel
%{common_description}

This package contains compatibility glue for code that still imports the
%{oldgoipath} Go namespace.


%prep
%forgeautosetup


%install
%goinstall

install -m 0755 -vd %{buildroot}%{gopath}/src/%(dirname %{oldgoipath})
ln -s %{gopath}/src/%{goipath} %{buildroot}%{gopath}/src/%{oldgoipath}


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%files -n compat-%{oldgoname}-devel
%dir %{gopath}/src/%(dirname %{oldgoipath})
%{gopath}/src/%{oldgoipath}


%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181026gitc42b0e3
- Add compat for old name

* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20181026gitc42b0e3
- Bump to commit c42b0e3b24d96976ecac81ef691662777b39ef64

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git91d1485
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180418git91d1485
- First package for Fedora

