# 🔍 Localhost Port Scanner

A lightweight Python tool to scan open ports on your local machine (`127.0.0.1`) and flag any that may be sensitive or unexpected.

---

## ⚙️ Features

- Scans ports 1–1024 by default
- Detects open ports
- Maps ports to running processes
- Highlights common sensitive ports (e.g. SSH, MySQL, Redis)
- Outputs a clean, color-coded table

---

## 🚀 Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

## 2. Run the scanner
```bash
python3 port_scanner.py
```
##### Optional: scan a custom port range by editing scan_ports(start, end)

## 🧪 Sample Output
```
🔍 Scanning ports 1–1024 on localhost...

+--------+------------+----------------+
| Port   | Service    | Process        |
+--------+------------+----------------+
| 22     | SSH        | sshd           |
| 80     | HTTP       | nginx          |
| 5432   | PostgreSQL | postgres       |
+--------+------------+----------------+
```
## 🔒 Notes
- Uses psutil to identify local processes
- Run as sudo if needed for accurate process info
- Default timeout: 0.5s per port
## 📝 License
- MIT
## 🙌 Contributions
- Star ⭐ it | Fork 🍴 it | Make it better 🚀