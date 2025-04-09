from scapy.all import ARP, Ether, srp

def arp_scan(network):
    arp_request = ARP(pdst=network)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request

    answered, _ = srp(arp_request_broadcast, timeout=2, verbose=False)

    devices = []
    for sent, received in answered:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def main():
    network = input("Enter network (e.g., 192.168.1.0/24): ")
    print(f"Scanning {network}...")

    devices = arp_scan(network)
    print("\nActice devices:")
    print("IP\t\t\tMAC Address")
    print("-" * 40)
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")

if __name__ == "__main__":
    main()