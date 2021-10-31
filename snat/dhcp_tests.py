from scapy.all import *


def dhcp_discover():
    conf.checkIPaddr = False
    fam,hw = get_if_raw_hwaddr(conf.iface)
    hw = RandMAC()
    l2 = Ether(dst="ff:ff:ff:ff:ff:ff")
    ip = IP(src="0.0.0.0",dst="255.255.255.255")
    udp= UDP(sport=68,dport=67)
    dhcp = DHCP(options=[("message-type","discover"),"end"])
    pkt = l2/ip/udp/BOOTP(chaddr=hw)/dhcp
    ans, unans = srp(pkt, multi=True, timeout=5)
    return ans

scan = dhcp_discover()
