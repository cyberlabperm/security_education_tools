from scapy.all import Ether, ARP, srp

def arp_scan(network):
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=network),timeout=2)
    return ans


network = "192.168.0.0/24"
for pkt in arp_scan(network):
    print(pkt)
