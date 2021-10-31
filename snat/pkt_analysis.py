from scapy.all import *

def pkt_comparision(pkt1, pkt2):
    model = list()
    for layer in pkt1.layers():
        for field in pkt1[layer].fields:
           model.append([layer, field])
    for layer in pkt2.layers():
        for field in pkt2[layer].fields:
            if [layer, field] not in model:
                model.append([layer, field])
    results = list()
    for item in model:
        if pkt1[item[0]].fields.get(item[1]) != pkt2[item[0]].fields.get(item[1]):
            print(f'{item[0]} {item[1]} 1: {pkt1[item[0]].fields.get(item[1])} 2: {pkt2[item[0]].fields.get(item[1])}')
            result = [item[0], item[1], pkt1[item[0]].fields.get(item[1]), pkt2[item[0]].fields.get(item[1])]
            results.append(result)
    return results

def filter_conn_list(conn_list, dport):
    results = list()
    for conn in conn_list:        
        if conn[3] == dport:
            results.append(conn)
    return results

def find_tcp_syn_pkts(pcap, dport=0):
    results = list()
    if dport == 0:
        for pkt in pcap:
            if pkt.haslayer('TCP') and pkt['TCP'].flags == "S":          
                results.append(pkt)
    else:
        for pkt in pcap:
            if pkt.haslayer('TCP') and pkt['TCP'].flags == "S" and pkt[TCP].dport == dport:          
                results.append(pkt) 
    return results


def find_tcp_conn(pcap):
    results = list()
    for pkt in pcap:
        if pkt.haslayer('TCP') and pkt['TCP'].flags == "S":
            result = pkt[IP].src, pkt[TCP].sport, pkt[IP].dst, pkt[TCP].dport
            if result not in results:                
                results.append(result)
    return results



