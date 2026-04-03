
# Network Port Scanner

A fast, multithreaded network port scanner written in Python that identifies open ports on a target host. This project demonstrates core cybersecurity and networking principles.

---

## Features

* Scans ports from 1 to 1024 (configurable)
* Multithreaded scanning for improved performance
* Uses TCP socket connections
* Displays all open ports found
* Clean and efficient code structure

---

## Technologies Used

* Python 3
* socket (network communication)
* concurrent.futures (multithreading)

---

## How It Works

* Prompts the user to enter a target IP address
* Attempts to connect to each port in the specified range
* Uses multiple threads to speed up scanning
* Identifies open ports based on successful connections
* Outputs a list of all detected open ports

---

## How to Run

* Make sure Python 3 is installed
* Save the script as `port_scanner.py`
* Run the program:

```bash
python port_scanner.py
```

* Enter the target IP address when prompted

---

### Disclaimer

This tool is intended for educational purposes only.
Only scan systems you own or have explicit permission to test.
