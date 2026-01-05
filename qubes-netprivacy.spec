# SPDX-FileCopyrightText: 2026 Bounty Contributors
# SPDX-License-Identifier: GPL-3.0-or-later

Name:           qubes-netprivacy
Version:        1.0
Release:        1%{?dist}
Summary:        Network privacy configuration tool for QubesOS

License:        GPL-3.0-or-later
URL:            https://github.com/SlowBearDigger/qubes-netprivacy-tool
Source0:        %{name}-%{version}.tar.gz

Requires:       python3
Requires:       NetworkManager
BuildArch:      noarch

%description
Simple CLI tool to configure MAC address randomization and IPv6 privacy
extensions on QubesOS dom0. Provides an easy way to enable network privacy
settings that apply at boot time.

%prep
%autosetup

%build
# No build needed for Python script

%install
install -D -m 755 qubes-netprivacy %{buildroot}%{_bindir}/qubes-netprivacy

%files
%{_bindir}/qubes-netprivacy
%doc README.md
%license LICENSE

%changelog
* Sat Jan 04 2026 Bounty Contributors - 1.0-1
- Initial release
- MAC randomization support (stable cloning)
- IPv6 privacy extensions
- Disable/remove configurations
