import socket
import threading
from datetime import datetime

# ── Common ports and their services ──────────────────────────────────────────
COMMON_PORTS = {
    21:   "FTP",
    22:   "SSH",
    23:   "Telnet",
    25:   "SMTP",
    53:   "DNS",
    80:   "HTTP",
    110:  "POP3",
    143:  "IMAP",
    443:  "HTTPS",
    445:  "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
    27017: "MongoDB"
}

# ── Results storage ───────────────────────────────────────────────────────────
open_ports = []
lock = threading.Lock()

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown")
            with lock:
                open_ports.append((port, service))
                print(f"  [OPEN] Port {port:<6} — {service}")

    except Exception:
        pass

def scan(host, start_port, end_port):
    print(f"\n{'═' * 50}")
    print(f"  🔍 Port Scanner")
    print(f"{'═' * 50}")
    print(f"  Target   : {host}")
    print(f"  Ports    : {start_port} — {end_port}")
    print(f"  Started  : {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'═' * 50}\n")

    # Resolve hostname to IP
    try:
        ip = socket.gethostbyname(host)
        if ip != host:
            print(f"  Resolved : {host} → {ip}\n")
    except socket.gaierror:
        print(f"  ❌ Could not resolve hostname: {host}")
        return

    # Create threads for faster scanning
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(host, port))
        threads.append(t)
        t.start()

        # Limit concurrent threads to avoid overload
        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []

    # Wait for remaining threads
    for t in threads:
        t.join()

    # Print summary
    print(f"\n{'═' * 50}")
    print(f"  Scan Complete — {datetime.now().strftime('%H:%M:%S')}")
    print(f"  Open ports found: {len(open_ports)}")
    print(f"{'═' * 50}\n")

def main():
    print("\n🔐 Python Port Scanner")
    print("─" * 30)
    print("⚠️  Only scan hosts you own or have permission to scan!\n")

    host = input("Enter target (hostname or IP): ").strip()
    
    print("\nScan options:")
    print("  1. Quick scan (common ports only)")
    print("  2. Custom range")
    choice = input("\nChoose (1/2): ").strip()

    if choice == "1":
        # Scan only common ports
        print(f"\n{'═' * 50}")
        print(f"  🔍 Quick Scan — Common Ports")
        print(f"{'═' * 50}")
        print(f"  Target  : {host}")
        print(f"  Started : {datetime.now().strftime('%H:%M:%S')}")
        print(f"{'═' * 50}\n")

        try:
            ip = socket.gethostbyname(host)
            if ip != host:
                print(f"  Resolved : {host} → {ip}\n")
        except socket.gaierror:
            print(f"  ❌ Could not resolve hostname: {host}")
            return

        threads = []
        for port in COMMON_PORTS.keys():
            t = threading.Thread(target=scan_port, args=(host, port))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print(f"\n{'═' * 50}")
        print(f"  Scan Complete — {datetime.now().strftime('%H:%M:%S')}")
        print(f"  Open ports found: {len(open_ports)}")
        print(f"{'═' * 50}\n")

    elif choice == "2":
        start = int(input("Start port: "))
        end   = int(input("End port: "))
        scan(host, start, end)

main()