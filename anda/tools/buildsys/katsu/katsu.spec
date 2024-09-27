# Generated by rust2rpm 26
%bcond_without check
%bcond_without mold

# prevent library files from being installed
%global cargo_install_lib 0

Name:           katsu
Version:        0.8.1
Release:        1%?dist
Summary:        Vicious image builder
Packager:       madonuko <mado@fyralabs.com>

SourceLicense:  MIT
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-3-Clause
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# Unlicense OR MIT
License:        (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-3-Clause AND MIT AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/FyraLabs/katsu
Source0:		%url/archive/refs/tags/v%version.tar.gz

BuildRequires:  anda-srpm-macros cargo-rpm-macros >= 26
Requires:		xorriso dracut limine grub2 systemd-devel squashfs-tools parted gdisk
Requires:		dracut-live dracut-config-generic dracut-config-rescue grub2-tools-extra dracut-squash
BuildRequires:	cargo rust-packaging pkgconfig(libudev) clang-devel

%description
Katsu is a tool for building bootable images from RPM based systems.
It is an alternative to Lennart Poettering's mkosi tool, designed to be robust,
fast, and easy to use while still providing many output formats.

%prep
%autosetup -p1
%cargo_prep_online

%build
#cargo_build
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/katsu

%changelog
* Mon Aug 19 2024 madonuko <mado@fyralabs.com> - 0.7.1-2
- Rewrite spec with rust2rpm
