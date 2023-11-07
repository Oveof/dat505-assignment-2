import socket
from scapy.all import *
from scapy.layers.inet import *
import sys


def send_ping(destination_address, message_count):
    send(IP(src=sys.argv[1], dst=destination_address) / ICMP()/"lol?", count=message_count)

def get_host_ip():
    hostname = socket.gethostname()
    ipv4_address = socket.gethostbyname(hostname)


