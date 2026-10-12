# Network Port Scanner & Vulnerability Detector

## Overview
A lightweight Python-based network reconnaissance tool designed to scan target IP addresses or domain names for open ports, perform service banner grabbing, and flag potential misconfigurations.

## Key Features
* **Multi-Port Scanning:** Scans standard well-known service ports (1–1024) or custom user-defined ranges.
* **Banner Grabbing:** Attempts to retrieve service identification strings to identify running versions (e.g., SSH, HTTP, FTP).
* **Error Handling:** Built-in safeguards against invalid IPs, host resolution failures, and user interrupts (`Ctrl+C`).

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/bilalkhantaraqai/python-port-scanner.git](https://github.com/bilalkhantaraqai/python-port-scanner.git)
   cd python-port-scanner