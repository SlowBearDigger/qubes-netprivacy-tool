# QubesOS Network Privacy Tool

CLI tool to configure MAC address randomization and IPv6 privacy extensions on QubesOS dom0.

## Installation

### From Source

```bash
wget https://raw.githubusercontent.com/SlowBearDigger/qubes-netprivacy-tool/main/qubes-netprivacy
chmod +x qubes-netprivacy
sudo mv qubes-netprivacy /usr/local/bin/
```

## Usage

```bash
# Enable MAC randomization
sudo qubes-netprivacy --enable-mac-random

# Enable IPv6 privacy
sudo qubes-netprivacy --enable-ipv6-privacy

# Disable all
sudo qubes-netprivacy --disable-all

# Restart NetworkManager to apply
sudo systemctl restart NetworkManager
```

## Features

- MAC address randomization (stable cloning)
- IPv6 privacy extensions (RFC 4941)
- Simple enable/disable

## Config Files

- `/etc/NetworkManager/conf.d/80_randomize-mac.conf`
- `/etc/NetworkManager/conf.d/80_ipv6-privacy.conf`
- `/etc/systemd/networkd.conf.d/80_ipv6-privacy-extensions.conf`

## License

GPL-3.0-or-later
