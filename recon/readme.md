# Recon Automation Tool

A simple Python-based reconnaissance automation tool for cybersecurity learning and basic information gathering.

## Features

- IP Address Resolution
- WHOIS Lookup
- DNS Enumeration
- Subdomain Discovery using crt.sh
- Common Port Scanning
- HTTP Header Collection

---

# Screenshot

```bash
[+] Starting Recon on example.com

[+] IP Address: 93.184.216.34

[+] WHOIS Information
...

[+] DNS Records
...

[+] Subdomains from crt.sh
api.example.com
mail.example.com

[+] Scanning Common Ports
[OPEN] Port 80
[OPEN] Port 443

[+] HTTP Headers
Server: nginx
Content-Type: text/html

[+] Recon Completed
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/recon-tool.git
cd recon-tool
```

## Install Requirements

```bash
pip install requests
```

---

# Usage

```bash
python3 recon.py
```

Enter target domain:

```bash
example.com
```

---

# Modules Used

- socket
- requests
- subprocess
- urllib.parse

---

# Future Improvements

- Nmap Integration
- Directory Fuzzing
- Multithreading
- Screenshot Capture
- Technology Detection
- JSON/TXT Export
- Shodan Integration
- ASN Lookup

---

# Legal Disclaimer

This tool is created for educational and authorized security testing purposes only.

Do NOT use this tool against systems without permission.

The author is not responsible for misuse or illegal activities.

---

# Author

Nasif(Burka)

Cybersecurity & Recon Automation Learning Project
