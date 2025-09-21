import joblib
import numpy as np
import datetime
import os
import pandas as pd

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
model_path = os.path.join(base_dir, 'model', 'ids_model_simple.pkl')

# Load model and label encoders
clf, label_encoders = joblib.load(model_path)

def extract_features(packet):
    try:
        # 1. protocol_type
        proto = packet.proto if hasattr(packet, 'proto') else None
        if proto == 6:
            protocol = 'tcp'
        elif proto == 17:
            protocol = 'udp'
        elif proto == 1:
            protocol = 'icmp'
        else:
            protocol = 'other'

        # 2. service (based on dport)
        dport = packet.dport if hasattr(packet, 'dport') else 0
        if dport == 80:
            service = 'http'
        elif dport == 21:
            service = 'ftp_data'
        elif dport == 22:
            service = 'ssh'
        elif dport == 443:
            service = 'https'
        else:
            service = 'other'

        # 3. flag (from TCP flags if available)
        flag = 'SF'
        if hasattr(packet, 'flags'):
            flag = str(packet.flags)

        # 4. src_bytes (size of payload)
        src_bytes = len(packet.payload) if hasattr(packet, 'payload') else 0

        # 5. dst_bytes — unavailable from single packet; default to 0
        dst_bytes = 0

        # Encode categorical features
        protocol_enc = label_encoders['protocol_type'].transform([protocol])[0] if protocol in label_encoders['protocol_type'].classes_ else 0
        service_enc = label_encoders['service'].transform([service])[0] if service in label_encoders['service'].classes_ else 0
        flag_enc = label_encoders['flag'].transform([flag])[0] if flag in label_encoders['flag'].classes_ else 0

        return [protocol_enc, service_enc, flag_enc, src_bytes, dst_bytes]

    except Exception as e:
        print("❌ Feature extraction error:", e)
        return None

def detect(packet):
    features = extract_features(packet)
    if features is None:
        return

    try:
        # Optional: Use DataFrame to suppress sklearn warning
        features_df = pd.DataFrame([features], columns=['protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes'])
        prediction = clf.predict(features_df)[0]

        if prediction == 'attack':
            alert = f"[{datetime.datetime.now()}] INTRUSION DETECTED! Features: {features}"
            print(alert)
            log_path = os.path.join(base_dir, "logs", "intrusion_logs.txt")
            with open(log_path, "a", encoding='utf-8') as f:
                f.write(alert + "\n")

    except Exception as e:
        print("❌ Detection error:", e)
