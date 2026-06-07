# 🔍 Python Port Scanner

> A multithreaded network port scanner built in Python — detects open ports and identifies running services on any target host.

[![Status](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/Sri-Janani01/port-scanner)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

**📁 Repository:** [github.com/Sri-Janani01/port-scanner](https://github.com/Sri-Janani01/port-scanner)

> ⚠️ Only scan hosts you own or have explicit permission to scan. Unauthorized port scanning may be illegal.

---

## 📸 Preview
<img width="641" height="449" alt="Screenshot 2026-06-07 at 4 32 53 PM" src="https://github.com/user-attachments/assets/503b9acc-7fc0-49ae-b346-26bb152a173e" />

---

## ✨ Features

- **Quick Scan** — scans common ports (HTTP, SSH, FTP, DNS, MySQL etc.)
- **Custom Range** — scan any port range you specify
- **Multithreaded** — scans up to 100 ports simultaneously for speed
- **Service Detection** — identifies what service is running on each open port
- **Hostname Resolution** — resolves domain names to IP addresses
- **Clean CLI output** — easy to read results with timestamps

---

## 🛡️ Cybersecurity Concepts Demonstrated

| Concept | Implementation |
|---------|---------------|
| Port Scanning | TCP connect scan using `socket` |
| Service Detection | Port-to-service mapping dictionary |
| Multithreading | `threading.Thread` for parallel scanning |
| Network Recon | Hostname resolution with `socket.gethostbyname` |
| Thread Safety | `threading.Lock` to prevent race conditions |

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| `socket` | TCP connection handling |
| `threading` | Parallel port scanning |
| `datetime` | Scan timestamps |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/Sri-Janani01/port-scanner.git
cd port-scanner

# 2. Run the scanner
python scanner.py
```

### Usage

---

## 🗺 Common Ports Reference

| Port | Service | Risk if Open |
|------|---------|-------------|
| 21 | FTP | Unencrypted file transfer |
| 22 | SSH | Brute force attacks |
| 80 | HTTP | Web vulnerabilities |
| 443 | HTTPS | Web vulnerabilities |
| 3306 | MySQL | Database exposure |
| 3389 | RDP | Remote desktop attacks |

---

## 🗺 Roadmap

- [ ] Save scan results to a file
- [ ] UDP port scanning
- [ ] OS detection
- [ ] Banner grabbing (get service version info)
- [ ] Scan multiple targets at once

---

## 👩‍💻 Author

**Sri Janani** — [github.com/Sri-Janani01](https://github.com/Sri-Janani01)

---

## 📄 License

MIT — for educational purposes only. Always get permission before scanning.
