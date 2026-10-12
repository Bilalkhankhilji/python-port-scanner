import socket
import sys
from datetime import datetime

def grab_banner(target_ip, port):
    """Attempt to grab service banner from an open port."""
    try:
        s = socket.socket()
        s.settimeout(1.5)
        s.connect((target_ip, port))
        s.send(b'HEAD / HTTP/1.1\r\nHost: ' + target_ip.encode() + b'\r\n\r\n')
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        s.close()
        return banner if banner else "No banner retrieved"
    except Exception:
        return "No banner retrieved"

def run_port_scanner():
    print("=" * 50)
    print("      Python Network Port & Vulnerability Scanner")
    print("=" * 50)
    
    target_host = input("\nEnter target IP address or hostname: ").strip()
    
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print("\n[!] Error: Hostname could not be resolved.")
        sys.exit()

    print("-" * 50)
    print(f"Scanning target IP : {target_ip}")
    print(f"Time started       : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 8080]

    try:
        for port in common_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target_ip, port))
            
            if result == 0:
                banner_info = grab_banner(target_ip, port)
                first_line_banner = banner_info.split('\n')[0]
                print(f"[+] Port {port:<5}: OPEN  | Banner: {first_line_banner[:40]}")
            s.close()
            
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
        sys.exit()
    except socket.error:
        print("\n[!] Could not connect to target host.")
        sys.exit()

    print("-" * 50)
    print("[+] Scan completed successfully.")

if __name__ == "__main__":
    run_port_scanner()