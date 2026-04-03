# Imports

import socket
from concurrent.futures import ThreadPoolExecutor

# Banner
 
def banner_scanner():
    title = "Port Scanner"
    author = "Made by: Pedro Gomes"
    width = max(len(title), len(author)) + 10  

    print("-" * width)
    print(title.center(width))
    print(author.center(width))
    print("-" * width)
    print("")

banner_scanner()

# Variables

TARGET_HOST = input("What is the ip you want to scan?")
START_PORT = 1
END_PORT = 1024
TIMEOUT = 0.5
MAX_THREADS = 100

print("")

# Core program

def scan_port(port: int):
   
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            result = sock.connect_ex((TARGET_HOST, port))
            if result == 0:
                return port
    except socket.error:
        pass
    return None


def main():
    print(f"Starting scan on {TARGET_HOST}...\n")

    open_ports = []

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        ports = range(START_PORT, END_PORT + 1)
        results = executor.map(scan_port, ports)

    for port in results:
        if port is not None:
            open_ports.append(port)

    print("Scan completed.\n")

    if open_ports:
        print("Open ports found:")
        for port in open_ports:
            print(f" - Port {port}")
    else:
        print("No open ports detected.")

if __name__ == "__main__":
    main()
