import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import socket

print("=" * 50)
print(" Simple Web Vulnerability Scanner ")
print("=" * 50)

target = input("\nEnter Target URL (http://example.com): ").strip()


def check_security_headers(url):
    print("\n[+] Checking Security Headers")

    try:
        response = requests.get(url, timeout=5)

        headers = response.headers

        security_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "Referrer-Policy"
        ]

        for header in security_headers:
            if header in headers:
                print(f"[FOUND] {header}")
            else:
                print(f"[-] Missing {header}")

    except Exception as e:
        print(f"[-] Error: {e}")



def test_sqli(url):
    print("\n[+] Testing SQL Injection")

    payloads = [
        "'",
        "\"",
        "' OR '1'='1",
        "\" OR \"1\"=\"1"
    ]

    sql_errors = [
        "sql syntax",
        "mysql",
        "syntax error",
        "unclosed quotation",
        "database error"
    ]

    for payload in payloads:
        test_url = url + payload

        try:
            response = requests.get(test_url, timeout=5)

            for error in sql_errors:
                if error.lower() in response.text.lower():
                    print(f"[Potential SQLi] Payload: {payload}")
                    return

        except:
            pass

    print("[-] No SQL Injection detected")



def test_xss(url):
    print("\n[+] Testing XSS")

    payload = "<script>alert('xss')</script>"

    try:
        response = requests.get(url + payload, timeout=5)

        if payload in response.text:
            print("[Potential XSS] Payload reflected")
        else:
            print("[-] No XSS detected")

    except Exception as e:
        print(f"[-] Error: {e}")



def admin_discovery(url):
    print("\n[+] Discovering Admin Pages")

    admin_paths = [
        "admin",
        "login",
        "dashboard",
        "administrator",
        "admin.php",
        "cpanel"
    ]

    for path in admin_paths:
        full_url = urljoin(url, path)

        try:
            response = requests.get(full_url, timeout=5)

            if response.status_code == 200:
                print(f"[FOUND] {full_url}")

        except:
            pass



def port_scan(domain):
    print("\n[+] Scanning Common Ports")

    ports = [21, 22, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]

    try:
        ip = socket.gethostbyname(domain)

        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f"[OPEN] Port {port}")

            sock.close()

    except Exception as e:
        print(f"[-] Error: {e}")



def detect_technology(url):
    print("\n[+] Detecting Technologies")

    try:
        response = requests.get(url, timeout=5)

        headers = response.headers

        if "Server" in headers:
            print(f"[Server] {headers['Server']}")

        if "X-Powered-By" in headers:
            print(f"[Powered By] {headers['X-Powered-By']}")

    except Exception as e:
        print(f"[-] Error: {e}")


# -----------------------------
# Crawl Links
# -----------------------------
def crawl_links(url):
    print("\n[+] Crawling Links")

    try:
        response = requests.get(url, timeout=5)

        soup = BeautifulSoup(response.text, "html.parser")

        links = set()

        for tag in soup.find_all("a"):
            href = tag.get("href")

            if href:
                full_link = urljoin(url, href)
                links.add(full_link)

        for link in links:
            print(link)

    except Exception as e:
        print(f"[-] Error: {e}")



domain = target.replace("http://", "").replace("https://", "").split("/")[0]

check_security_headers(target)
test_sqli(target)
test_xss(target)
admin_discovery(target)
port_scan(domain)
detect_technology(target)
crawl_links(target)

print("\n[+] Scan Completed")
