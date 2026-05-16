# Web Vulnerability Scanner

A simple Python-based web vulnerability scanner designed for cybersecurity learning and basic security assessment.

## Features

- Detects common web vulnerabilities
- SQL Injection testing
- XSS detection
- Security Header Analysis
- Open Port Detection
- Admin Page Discovery
- Technology Fingerprinting
- Basic Crawling
- HTTP Response Analysis

---

# Screenshot

```bash
[+] Starting Scan on target.com

[+] Checking Security Headers
[-] Missing X-Frame-Options
[-] Missing Content-Security-Policy

[+] Testing SQL Injection
[Potential SQLi] Parameter vulnerable: id

[+] Testing XSS
[Potential XSS] Reflected payload detected

[+] Discovering Admin Panels
[FOUND] /admin
[FOUND] /login

[+] Scan Completed
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/web-vulnerability-scanner.git
cd web-vulnerability-scanner
```

## Install Requirements

```bash
pip install requests beautifulsoup4
```

---

# Usage

```bash
python3 scanner.py
```

Enter target URL:

```bash
http://example.com
```

---

# Vulnerabilities Checked

- SQL Injection (Basic)
- Cross-Site Scripting (XSS)
- Missing Security Headers
- Open Directories
- Exposed Admin Panels
- Information Disclosure
- Server Fingerprinting

---

# Project Structure

```bash
web-vulnerability-scanner/
│
├── scanner.py
├── payloads/
│   ├── sqli.txt
│   └── xss.txt
├── wordlists/
│   └── admin-panels.txt
├── reports/
└── README.md
```

---

# Future Improvements

- Multithreading
- HTML Report Generation
- CVE Detection
- Authentication Support
- Cookie Analysis
- CSRF Detection
- API Security Testing
- WAF Detection

---

# Legal Disclaimer

This tool is created strictly for:

- Educational Purposes
- Authorized Security Testing
- Ethical Hacking Labs
- CTF Practice

Do NOT scan systems without permission.

Unauthorized testing may violate laws and regulations.

The author is not responsible for misuse.

---

# Author

Nasif(Burka)

Cybersecurity Learning Project
