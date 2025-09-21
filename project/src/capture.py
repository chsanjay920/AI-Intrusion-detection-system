from scapy.all import sniff, IP, TCP, UDP, ICMP
from detect_intrusions import detect

print("Starting packet sniffing...")

def process_packet(packet):
    if IP in packet:
        if TCP in packet or UDP in packet or ICMP in packet:
            detect(packet)

# Start sniffing (interface can be specified with `iface="Ethernet"` etc.)
sniff(filter="ip", prn=process_packet, store=0)
