%global commit 	c4102fe4eef8c0539c03d60c7256fd4bc599bf4a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           crossystem
Summary:        Manage ChromeOS firmware
License:        BSD-3-Clause
URL:            https://chromium.googlesource.com/chromiumos/platform/vboot_reference/

Version:        %shortcommit
Release:        15278.B%{?dist}
Source0:        https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+archive/refs/heads/release-R110-15278.B.tar.gz
Patch0:		use-flashrom-cros.patch
Patch1:		disable-werror.patch

#Requires:	flashrom-cros
BuildRequires:  make gcc openssl-devel flashrom-devel libuuid-devel

%description
A tool to manage ChromeOS bootloader flags and get various
info from a ChromeOS system

%prep
%autosetup -c

%build
%make_build

%install
install -Dm755 build/utility/crossystem %{buildroot}%{_bindir}/crossystem

%files
%license LICENSE
%{_bindir}/crossystem

%changelog
