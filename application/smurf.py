import socket
from scapy.all import *
from scapy.layers.inet import *
import sys
import ipaddress

def send_ping(destination_address, broadcast_address, message_count):
    send(IP(src=destination_address, dst=broadcast_address) / ICMP()/"test", count=message_count)

def get_broadcast_address(ip_address, network_mask):
    host = ipaddress.IPv4Address(ip_address)
    network = ipaddress.IPv4Network(ip_address + '/' + MASK, False)
    return net.broadcast_address


def get_host_ip():
    hostname = socket.gethostname()
    ipv4_address = socket.gethostbyname(hostname)


