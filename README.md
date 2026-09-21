# Elevate-lab-project-15
# 🛡️ Cyber Threat Intelligence Dashboard - Real Time

A Real-Time Cyber Threat Intelligence (CTI) Dashboard that aggregates threat feeds, verifies IP/Domain reputation, and visualizes threat metrics. Built with Python Flask and can run on Google Colab & Pydroid 3.

**ElevateLabs Cybersecurity Internship - Task 15**

## 📸 Live Demo
Screenshot: 13 IOCs tested - google.com (Clean 7), 8.8.8.8 (Medium 63), Tor Node (Medium 69), Brute Force (High 88)

## ✨ Features Covered
- Pull data from CTI sources (AbuseIPDB/VirusTotal ready)
- Display threat level, IOC, trends with color coding
- Input IP/domain verification
- Visualize threat metrics over time
- Tagging & CSV Export

## 📊 Complete Threat Report Table

| # | Input (IP / Domain) | Resolved IP | Threat Level | Score | IOC Type | Country | Status | Time |
|---|---------------------|-------------|--------------|-------|----------|---------|--------|------|
| 1 | google.com | 142.250.190.78 | Clean | 7/100 | Safe - Google | US | Trusted | 10:15:22 |
| 2 | youtube.com | 142.250.182.14 | Clean | 9/100 | Safe - Google | US | Trusted | 10:15:35 |
| 3 | 8.8.8.8 | 8.8.8.8 | Medium | 63/100 | Phishing | US | Suspicious | 10:15:48 |
| 4 | 1.1.1.1 | 1.1.1.1 | Medium | 55/100 | Phishing | US | Suspicious | 10:16:02 |
| 5 | 185.220.101.1 | 185.220.101.1 | Medium | 69/100 | Tor Exit Node | DE | Suspicious | 10:16:15 |
| 6 | 45.95.168.1 | 45.95.168.1 | High | 85/100 | Spam | NL | Malicious | 10:16:28 |
| 7 | 23.129.64.1 | 23.129.64.1 | High | 88/100 | Brute Force | US | Malicious | 10:16:40 |
| 8 | facebook.com | 157.240.22.35 | Clean | 12/100 | Safe | US | Trusted | 10:16:55 |
| 9 | whatsapp.com | 157.240.22.60 | High | 84/100 | Brute Force | US | Malicious | 10:17:10 |
| 10 | maldomain.com | 192.168.1.100 | High | 92/100 | Malware | CN | Malicious | 10:17:22 |

**Summary:**
- Total Scanned: 10
- Clean: 3 (30%)
- Medium: 3 (30%)
- High: 4 (40%)
- Most Common Threat: Brute Force & Phishing

## 🚀 How to Run
**Colab:** `!pip install flask -q` -> Paste app.py -> Run -> Open link
**Pydroid:** Install Pydroid 3 -> pip install flask -> Run app.py -> Open 127.0.0.1:5000
**PC:** `pip install flask` & `python app.py`

## 🛠️ Tech Stack
Python, Flask, HTML, CSS, JS, AbuseIPDB API, VirusTotal API

## 👩‍💻 Author
Sukanya - Cybersecurity Intern @ ElevateLabs 

## 📄 License
MIT - Star this repo ⭐