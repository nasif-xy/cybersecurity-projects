# Advanced Nmap Automation Tool

A powerful Python-based Nmap automation tool for reconnaissance, service enumeration, vulnerability detection, and network scanning.

This project automates multiple advanced Nmap scans with multithreading and exports results into JSON and TXT reports.

---

# Features

- Fast Port Scanning
- Service Version Detection (`-sV`)
- OS Detection (`-O`)
- Aggressive Scanning (`-A`)
- Vulnerability Detection using NSE Scripts (`--script vuln`)
- Multithreaded Scanning
- JSON Report Export
- TXT Report Export
- Protocol Enumeration
- Service Fingerprinting

---

# Screenshot

```bash
============================================================
 Advanced Nmap Automation Tool
============================================================

Enter Target IP or Domain: scanme.nmap.org

[+] Running Fast Scan...
[+] Running Service Version Detection...
[+] Running OS Detection...
[+] Running Aggressive Scan...
[+] Running Vulnerability Scan...

[Fast Scan] scanme.nmap.org:22 ssh OpenSSH 8.2
[Service Version Detection] scanme.nmap.org:80 http Apache httpd
[OS Detection] Linux 5.X
[Vulnerability Scan] NSE vulnerabilities checked

[+] TXT Report Saved: scan_report_scanme.nmap.org.txt
[+] JSON Report Saved: scan_report_scanme.nmap.org.json

[+] All Scans Completed Successfully
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/advanced-nmap-tool.git
cd advanced-nmap-tool
```

---

# Requirements

## Install Python Dependency

```bash
pip install python-nmap
```

## Install Nmap

### Linux

```bash
sudo apt install nmap
```

### Windows

Download Nmap from:

:contentReference[oaicite:0]{index=0}

---

# Usage

Run the tool:

```bash
python3 advanced_nmap_tool.py
```

Enter target:

```bash
scanme.nmap.org
```

---

# Scan Types Included

| Scan Type | Description |
|---|---|
| `-F` | Fast scan on common ports |
| `-sV` | Detect service versions |
| `-O` | Detect operating system |
| `-A` | Aggressive scan |
| `--script vuln` | Run vulnerability detection scripts |

---

# Output Reports

The tool automatically saves:

- TXT Report
- JSON Report

Example:

```bash
scan_report_example.com.txt
scan_report_example.com.json
```

---

# Project Structure

```bash
advanced-nmap-tool/
│
├── advanced_nmap_tool.py
├── reports/
├── README.md
└── requirements.txt
```

---

# Future Improvements

- HTML Dashboard Report
- Live Scan Progress Bar
- Telegram Notifications
- Discord Webhook Alerts
- CVE Lookup Integration
- UDP Scanning (`-sU`)
- Stealth SYN Scan (`-sS`)
- GeoIP Tracking
- ASN Enumeration
- Network Range Scanning
- Web-Based GUI

---

# Legal Disclaimer

This tool is intended strictly for:

- Educational Purposes
- Authorized Security Testing
- CTF Challenges
- Ethical Hacking Labs

Do NOT scan targets without proper authorization.

Unauthorized scanning may violate laws and regulations.

The author is not responsible for misuse.

---

# Author

Nasif(Burka)

Cybersecurity & Recon Automation Project
