import socket
import requests
import subprocess
from urllib.parse import urlparse

target = input("Enter target domain: ").strip()

print(f"\n[+] Starting Recon on {target}\n")


try:
    ip = socket.gethostbyname(target)
    print(f"[+] IP Address: {ip}")
except:
    print("[-] Could not resolve domain")
    exit()


print("\n[+] WHOIS Information")
try:
    subprocess.run(["whois", target])
except:
    print("[-] WHOIS command not installed")


print("\n[+] DNS Records")
try:
    subprocess.run(["nslookup", target])
except:
    print("[-] nslookup not found")


print("\n[+] Subdomains from crt.sh")

try:
    url = f"https://crt.sh/?q=%25.{target}&output=json"
    response = requests.get(url, timeout=10)

    data = response.json()

    subdomains = set()

    for entry in data:
        name = entry['name_value']
        for sub in name.split("\n"):
            subdomains.add(sub.strip())

    for sub in sorted(subdomains):
        print(sub)

except Exception as e:
    print("[-] Error fetching subdomains:", e)


print("\n[+] Scanning Common Ports")

common_ports = [21, 22, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]

for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f"[OPEN] Port {port}")

    sock.close()


print("\n[+] HTTP Headers")

try:
    r = requests.get(f"http://{target}", timeout=5)

    for key, value in r.headers.items():
        print(f"{key}: {value}")

except:
    print("[-] Could not fetch headers")

print("\n[+] Recon Completed")
