
# 🔐 AI-Powered Real-Time Intrusion Detection System (IDS)

A lightweight real-time Intrusion Detection System (IDS) using machine learning and packet sniffing. It monitors live network traffic, extracts meaningful features from packets, and classifies traffic as **normal** or **malicious** using a model trained on the NSL-KDD dataset.

---

## 🚀 Features

- Real-time packet sniffing using **Scapy**
- Machine learning model trained on **NSL-KDD**
- Detects malicious traffic patterns based on 5 extracted features
- Logs intrusion alerts with timestamps
- Clean modular code structure for easy customization

---

## 📂 Project Structure

project/
├── data/
│ └── NSL-KDD/ # Raw NSL-KDD dataset files
├── logs/
│ └── intrusion_logs.txt # Alerts saved here
├── model/
│ └── ids_model_simple.pkl # Trained RandomForest model
├── src/
│ ├── train_model.py # Trains and saves the model
│ ├── capture.py # Real-time packet capture
│ └── detect_intrusions.py # Feature extraction and detection logic
├── requirements.txt # Python dependencies
└── readme.md # You are here

yaml
Copy code

---

## 🛠️ Tech Stack

| Tool            | Purpose                     |
|-----------------|-----------------------------|
| Python          | Main programming language   |
| Scapy           | Packet sniffing             |
| pandas, NumPy   | Data preprocessing          |
| scikit-learn    | Model training              |
| joblib          | Model saving/loading        |

---

## 📦 Installation

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ids-project.git
cd ids-project
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
📊 Dataset: NSL-KDD
We use the improved NSL-KDD dataset instead of the outdated KDD99.

Download it from:
🔗 https://www.unb.ca/cic/datasets/nsl.html

Required files:

KDDTrain+.txt

KDDTest+.txt

KDDFeatureNames.txt

Place them in:

kotlin
Copy code
data/NSL-KDD/
🧠 Model Training
Run this once to train and save the model:

bash
Copy code
python src/train_model.py
Uses only 5 core features for real-time speed:

protocol_type

service

flag

src_bytes

dst_bytes

Output: model/ids_model_simple.pkl

⚡ Start Real-Time Intrusion Detection
bash
Copy code
python src/capture.py
Console will show:

Copy code
🚨 Starting packet sniffing...
When suspicious packets are detected:

less
Copy code
[2025-09-14 20:18:52.735518] 🚨 INTRUSION DETECTED! Features: [0, 44, 9, 0, 0]
Alerts are saved in:

bash
Copy code
logs/intrusion_logs.txt
🧪 How to Simulate an Intrusion
Run any of the following:

🔹 Option 1: nmap SYN scan
bash
Copy code
nmap -sS 127.0.0.1
🔹 Option 2: UDP flood test
python
Copy code
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for _ in range(100):
    sock.sendto(b"test", ("127.0.0.1", 9999))
    time.sleep(0.1)
🔹 Option 3: Use hping3
bash
Copy code
sudo hping3 -S 127.0.0.1 -p 22 -c 5
📌 Sample Output
less
Copy code
[2025-09-14 20:19:22.901665] 🚨 INTRUSION DETECTED! Features: [0, 44, 9, 0, 0]
📌 Known Warnings (and fixes)
Message	Fix
X does not have valid feature names	Wrap input in DataFrame
libpcap not available	Ignore on Windows; Scapy works
charmap can't encode emoji	File logging now uses utf-8 encoding

📈 Future Improvements
Expand model to use all 41 NSL-KDD features

Add automatic IP blocking

Build a web dashboard (e.g., Streamlit)

Add email or Slack notifications

Run as a background service or system daemon

👨‍💻 Author
Built with 💻 by [Your Name]
Inspired by research in AI-powered intrusion detection systems.

📝 License
This project is licensed under the MIT License. See LICENSE for details.

yaml
Copy code

---

### ✅ Next Steps

- Replace `[Your Name]` and the GitHub repo link with your actual info.
- Optionally, add screenshots or logs in the README using markdown image syntax.

Would you also like a version with screenshots or a `LICENSE` file generated?