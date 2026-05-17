import nmap
import json
import threading
from datetime import datetime

print("=" * 60)
print(" Advanced Nmap Automation Tool ")
print("=" * 60)

target = input("\nEnter Target IP or Domain: ").strip()

scanner = nmap.PortScanner()

results = {}


def run_scan(scan_name, arguments):

    print(f"\n[+] Running {scan_name} Scan...\n")

    try:
        scanner.scan(target, arguments=arguments)

        results[scan_name] = {}

        for host in scanner.all_hosts():

            host_data = {
                "state": scanner[host].state(),
                "protocols": {},
            }

            # OS Detection
            if 'osmatch' in scanner[host]:
                host_data["os"] = scanner[host]['osmatch']

            for protocol in scanner[host].all_protocols():

                ports_data = {}

                ports = scanner[host][protocol].keys()

                for port in sorted(ports):

                    port_info = scanner[host][protocol][port]

                    ports_data[port] = {
                        "state": port_info.get("state"),
                        "service": port_info.get("name"),
                        "product": port_info.get("product"),
                        "version": port_info.get("version"),
                        "extra_info": port_info.get("extrainfo")
                    }

                    print(f"[{scan_name}] {host}:{port} "
                          f"{port_info.get('name')} "
                          f"{port_info.get('product')} "
                          f"{port_info.get('version')}")

                host_data["protocols"][protocol] = ports_data

            results[scan_name][host] = host_data

    except Exception as e:
        print(f"[-] Error in {scan_name}: {e}")



scan_types = [
    ("Fast Scan", "-T4 -F"),
    ("Service Version Detection", "-sV"),
    ("OS Detection", "-O"),
    ("Aggressive Scan", "-A"),
    ("Vulnerability Scan", "--script vuln")
]

threads = []


for scan_name, arguments in scan_types:

    thread = threading.Thread(
        target=run_scan,
        args=(scan_name, arguments)
    )

    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


txt_file = f"scan_report_{target}.txt"

with open(txt_file, "w") as file:

    file.write("=" * 60 + "\n")
    file.write("Advanced Nmap Scan Report\n")
    file.write("=" * 60 + "\n")
    file.write(f"Target: {target}\n")
    file.write(f"Date: {datetime.now()}\n\n")

    for scan_name, data in results.items():

        file.write(f"\n### {scan_name} ###\n")

        for host, info in data.items():

            file.write(f"\nHost: {host}\n")
            file.write(f"State: {info['state']}\n")

            if "os" in info:
                file.write(f"OS Matches: {info['os']}\n")

            for protocol, ports in info["protocols"].items():

                file.write(f"\nProtocol: {protocol}\n")

                for port, details in ports.items():

                    file.write(
                        f"Port {port} | "
                        f"{details['service']} | "
                        f"{details['product']} | "
                        f"{details['version']} | "
                        f"{details['state']}\n"
                    )

print(f"\n[+] TXT Report Saved: {txt_file}")

json_file = f"scan_report_{target}.json"

with open(json_file, "w") as file:
    json.dump(results, file, indent=4)

print(f"[+] JSON Report Saved: {json_file}")

print("\n[+] All Scans Completed Successfully")