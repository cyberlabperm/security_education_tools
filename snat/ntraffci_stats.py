from scapy.all import *
import matplotlib.pyplot as plt 
import time
tcpdump = PcapReader('bruteforce_2.pcap')
time_list = list()
i = 0
j = 0
time0 = 0
timestep = 45
time1 = timestep
y = list()
x = list()
for pkt in tcpdump:
    if i == 0:
        syn_time = int(pkt.time)
        print('time of fisr pkt = ', time.ctime(int(pkt.time)))
        i +=1
    if pkt.haslayer(TCP) and pkt[TCP].flags == 'S':
        time_list.append(int(pkt.time) - syn_time)
        i += 1
print('time of last pkt = ', time.ctime(int(pkt.time)))
print('total pkts = ', i)
for i in range(0, len(time_list)):
    if time0 <= time_list[i] and time_list[i] < time1:
        j += 1
    else:
        x.append(time1)
        y.append(j)
        j = 1
        time0 += timestep
        time1 += timestep       
plt.figure(figsize=(9, 3))
plt.title('pkt in minute')
plt.xlabel('seconds')
plt.ylabel('pkts')
plt.plot(x, y)
#plt.bar(x,y)
plt.show()
