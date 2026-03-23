from scapy.all import sniff
from backend.sniffer.parser import parse_packet
from backend.ai.detector import detect_anomaly
from backend.sniffer.features import extract_features

def process(packet):
    parsed = parse_packet(packet)
    features = extract_features(packet)

    if parsed:
        result = detect_anomaly(features)
        print(parsed, "=>", result)

def start_capture():
    sniff(prn=process, store=False)
