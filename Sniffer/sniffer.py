from scapy.all import sniff
from sniffer.parser import parse_packet
from sniffer.filters import packet_filter

def process_packet(packet):
    if packet_filter(packet):
        parsed = parse_packet(packet)
        if parsed:
            print(parsed)

def start_sniffing(interface=None):
    sniff(iface=interface, prn=process_packet, store=False)
