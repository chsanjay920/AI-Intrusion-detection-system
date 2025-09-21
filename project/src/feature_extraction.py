from scapy.layers.inet import IP, TCP, UDP, ICMP

def extract_features(packet):
    try:
        features = {}
        if IP in packet:
            ip_layer = packet[IP]
            features['src_ip'] = ip_layer.src
            features['dst_ip'] = ip_layer.dst
            features['proto'] = ip_layer.proto
            features['len'] = len(packet)
            
            if TCP in packet:
                features['sport'] = packet[TCP].sport
                features['dport'] = packet[TCP].dport
                features['flags'] = int(packet[TCP].flags)
            elif UDP in packet:
                features['sport'] = packet[UDP].sport
                features['dport'] = packet[UDP].dport
                features['flags'] = 0
            elif ICMP in packet:
                features['sport'] = 0
                features['dport'] = 0
                features['flags'] = 0
            else:
                return None
            
            return [
                features['proto'],
                features['len'],
                features['sport'],
                features['dport'],
                features['flags']
            ]
    except Exception as e:
        print("❌ Error in feature extraction:", e)
    return None
