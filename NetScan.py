from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    # Create an ARP request
    arp = ARP(pdst=ip_range)
    # Create the Ethernet frame
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the Ethernet frame and the ARP request into a packet
    packet = ether / arp 
    # Send the packet and capture the response
    result = srp(packet, timeout=3, verbose=0)[0]

    # Parse the result
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

if __name__ == "__main__":
    # Define the IP range for your network
    ip_range = "192.168.1.1/100"
    devices = scan_network(ip_range)

    print("Available devices in the network:")
    for device in devices:
        print(f"IP: {device['ip']} MAC: {device['mac']}")
