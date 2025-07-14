import socket
import psutil
from tabulate import tabulate
from colorama import Fore, Style

# Ports we flag as sensitive
SENSITIVE_PORTS = {
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    6379: "Redis",
    5432: "PostgreSQL"
}

def is_port_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        result = s.connect_ex(('127.0.0.1', port))
        return result == 0

def get_process_using_port(port):
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port == port and conn.status == psutil.CONN_LISTEN:
            try:
                return psutil.Process(conn.pid).name()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                return "Unknown"
    return "-"

def scan_ports(start=1, end=1024):
    print(f"\n🔍 Scanning ports {start}–{end} on localhost...\n")
    open_ports = []

    for port in range(start, end + 1):
        if is_port_open(port):
            process = get_process_using_port(port)
            label = SENSITIVE_PORTS.get(port, "")
            color = Fore.RED if port in SENSITIVE_PORTS else Fore.GREEN
            open_ports.append([
                f"{color}{port}{Style.RESET_ALL}",
                label,
                process
            ])

    if open_ports:
        print(tabulate(open_ports, headers=["Port", "Service", "Process"], tablefmt="pretty"))
    else:
        print("✅ No open ports found in specified range.")

if __name__ == "__main__":
    scan_ports()
