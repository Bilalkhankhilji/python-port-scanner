#!/usr/bin/env python3
# ==============================================================================
# Script Name: scanner.py
# Description: Multi-threaded Python Port Scanner & Banner Grabber
# Author: Muhammad Bilal | Assistant Network Administrator
# ==============================================================================

import argparse
import socket
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def scan_port(target_ip, port):
    """Attempt a TCP connection on a given port and grab service banner if open."""
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            result = s.connect_ex((target_ip, port))
            
            if result == 0:
                service = "Unknown"
                banner = ""
                
                # Attempt basic banner grabbing for common ports
                try:
                    if port == 80 or port == 443:
                        service = "HTTP/HTTPS"
                    elif port == 22:
                        service = "SSH"
                        s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
                        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                    elif port == 21:
                        service = "FTP"
                        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                    else:
                        service = socket.getservbyport(port, 'tcp')
                except Exception:
                    pass

                print(f"[+] PORT {port}/tcp: OPEN ({service}) {banner}")
                return port
    except Exception as e:
        pass
    return None

def main():
    parser = argparse.ArgumentParser(description="Multi-threaded Python Port Scanner")
    parser.add_argument("--target", required=True, help="Target IP address or domain name")
    parser.add_argument("--ports", default="1-1024", help="Port range to scan (e.g., 1-1024 or 22,80,443)")
    parser.add_argument("--threads", type=int, default=50, help="Number of concurrent threads (default: 50)")
    
    args = parser.parse_args()
    
    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"[-] Error: Could not resolve hostname {args.target}")
        sys.exit(1)

    print("=" * 60)
    print(f"[+] Scanning Target: {target_ip} ({args.target})")
    print(f"[+] Time Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Parse port range
    ports_to_scan = []
    if "-" in args.ports:
        start_port, end_port = map(int, args.ports.split("-"))
        ports_to_scan = range(start_port, end_port + 1)
    elif "," in args.ports:
        ports_to_scan = [int(p) for p in args.ports.split(",")]
    else:
        ports_to_scan = [int(args.ports)]

    open_ports = []
    start_time = datetime.now()

    # Use ThreadPoolExecutor for fast multi-threaded port scanning
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = {executor.submit(scan_port, target_ip, port): port for port in ports_to_scan}
        for future in futures:
            port = future.result()
            if port:
                open_ports.append(port)

    duration = datetime.now() - start_time
    print("=" * 60)
    print(f"[+] Scan Complete in {duration.total_seconds():.2f} seconds.")
    print(f"[+] Total Open Ports Found: {len(open_ports)}")
    print("=" * 60)

if __name__ == "__main__":
    main()