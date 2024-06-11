%global repo_url https://github.com/ERGO-Code/HiGHS

Name:           highs
Version:        1.7.1
Release:        %autorelease
Summary:        High-performance linear optimization software

License:        MIT
URL:            https://highs.dev/
Source0:        %{repo_url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake >= 3.15
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  g++
%else
BuildRequires:  gcc
%endif

%description
HiGHS is a high performance serial and parallel solver for large scale sparse linear
optimization problems.


%package devel
Summary: Development files for HiGHS
Requires: highs = %{version}-%{release}

%description devel
Development libraries and headers for the HiGHS solver.


%prep
%autosetup -n HiGHS-%{version}


%build
%cmake -DFAST_BUILD=ON
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE.txt
%doc README.md
%{_bindir}/highs
%{_libdir}/libhighs.so*

%files devel
%{_includedir}/highs/*
%{_includedir}/highs_export.h
%{_libdir}/cmake/highs/*
%{_libdir}/libhighs.so
%{_libdir}/pkgconfig/highs.pc


%changelog
%if 0%{?fedora}
%autochangelog
%else
* Wed Aug 16 2023 Matěj Grabovský <matej@mgrabovsky.net> - 1.5.4-1
- Initial package for HiGHS upstream version 1.5.4
%endif

