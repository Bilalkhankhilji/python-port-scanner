# 🔍 Python Multi-Threaded Port Scanner & Banner Grabber

A lightweight, high-performance TCP port scanner and banner grabbing utility built in Python. Designed for rapid network reconnaissance, service identification, and security auditing.

**Author:** Muhammad Bilal — Assistant Network Administrator  
**Language:** Python 3  

---

## 🚀 Key Features
- **Multi-Threaded Performance:** Utilizes `ThreadPoolExecutor` to scan large port ranges concurrently in seconds.
- **Service & Banner Grabbing:** Automatically detects open ports and attempts to retrieve banner strings (e.g., HTTP, SSH, FTP versions).
- **Flexible Targets & Ranges:** Supports custom IP addresses, hostnames, and specific port ranges or comma-separated lists.
- **Clean CLI Interface:** Powered by Python's built-in `argparse` module for clean command-line operation.

---

## 🛠️ Usage & Syntax

Run the script from your terminal with `--target`:

### 1. Basic Scan (Default ports 1-1024)
```bash
python3 scanner.py --target 127.0.0.1

python3 scanner.py --target scanme.nmap.org --ports 1-100 --threads 100

python3 scanner.py --target 192.168.1.1 --ports 21,22,80,443,8080

📋 Command-Line Arguments
Argument          Description                                           Default
--target          Target IP address or domain name to scan              Required
--ports           Port range (1-1024) or specific ports (22,80,443)     1-1024
--threads         Number of concurrent execution threads                50