# 🛡️ Smart Incident Triage (ML-Powered)

A Python-based incident triage tool built for cybersecurity operations (SOC). This project automatically classifies, prioritizes, and routes security alerts using a machine learning model trained on real-world-style data.

---

## 🚀 Features

- 🧠 **Machine learning classification** (Phishing, Spam, Benign)
- 📂 Parses incident data from JSON
- 🚨 Assigns severity (High, Medium, Low)
- 📬 Routes to appropriate response teams
- 📄 Exports results to CSV
- 🔧 CLI interface with input/output flags

---

## 🗂️ Project Structure

Smart_Incident_Triage/
├── data/ # Sample and labeled incident data (JSON)
├── models/ # Saved ML model (.pkl)
├── src/ # All source code files
│ ├── main.py # CLI entry point
│ ├── load_incidents.py
│ ├── ml_classifier.py
│ ├── train_model.py
│ ├── triage_engine.py
│ ├── routing_engine.py
│ └── export_results.py
├── requirements.txt # Python dependencies
└── README.md


---

🚀 Quick Start
```markdown
1. Install Python packages
```bash
pip install -r requirements.txt

2. Train the model
python src/train_model.py

3. Run the triage tool
python src/train_model.py

4. Optional CLI input/Output
python src/main.py -i data/sample_incidents.json -o results.csv

📌 Example Output (Terminal)
--- Incident 1 ---
Subject: Urgent: Action Required - Microsoft Password Expiring
Category: Phishing
Priority: High
Team: Email Security Team

🧠 Tech Stack
Python 3

scikit-learn

joblib

TfidfVectorizer

yaml

---

You're now ready to drop this into GitHub and watch your profile shine. Want help addi
