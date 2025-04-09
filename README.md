# Simple Network Scanner

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Scapy](https://img.shields.io/badge/Scapy-2.4+-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A lightweight ARP-based network scanner to discover active devices on your local network.

## Features

- 🕵️‍♂️ **ARP Discovery** - Identify all connected devices
- 📋 **Clean Output** - Tabular display of IP/MAC addresses
- 🚀 **Fast Scanning** - Typically completes in 2-5 seconds
- 🛠️ **Single-File Tool** - No complex setup required

## Installation

```bash
# Install Scapy (requires root for raw sockets)
pip install scapy
```
## Usage
```bash
# Linux
sudo python3 network_scanner.py

# Windows
python network_scanner.py
```
## Example
```bash
Enter network to scan (e.g., 192.168.1.0/24): 192.168.1.0/24

Active Devices:
IP Address        MAC Address        
------------------------------
192.168.1.1      00:11:22:33:44:55
192.168.1.100    aa:bb:cc:dd:ee:ff
```
