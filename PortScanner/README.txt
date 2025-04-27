README

This Python script uses the `nmap` module to perform port scanning on a given IP address. The script offers the user the option to perform one of three types of scans: a SYN ACK scan (TCP), a UDP scan, or a comprehensive scan. It provides the status of the IP address, the open ports, and other related information.

### Requirements
- Python 3.x
- The `nmap` Python module (`python-nmap`)
- Nmap installed on your system

You can install the `python-nmap` module using pip:

To install Nmap (if not already installed):
- On Linux: `sudo apt install nmap`
- On macOS: `brew install nmap`
- On Windows: Download and install Nmap from [here](https://nmap.org/download.html).

### How to Run
1. Save the script as `nmap_scanner.py`.
2. Open a terminal (or command prompt) and navigate to the directory where the script is located.
3. Run the script using Python:

### Script Workflow
1. The script first welcomes the user and asks for the IP address to scan.
2. The user is then prompted to select a scanning option:
- **1. SYN ACK Scan (TCP)**: A simple TCP scan to identify open ports using SYN packets.
- **2. UDP Scan**: A scan for open UDP ports on the target.
- **3. Comprehensive Scan**: A more thorough scan that includes version detection, script scanning, OS detection, and more.
3. The script then uses Nmap to scan the provided IP address based on the selected option.
4. After the scan, the script prints the following information:
- Nmap scanner version
- Scan details
- IP status (Up or Down)
- Open ports for the selected protocol (TCP or UDP)

### Sample Output

### Notes
- The script scans ports from 1 to 1024 for the selected protocol (TCP or UDP).
- For TCP scans, the script performs a SYN scan using `-sS`.
- For UDP scans, the script uses `-sU`.
- The comprehensive scan uses a combination of flags (`-sS -sV -sC -A -O`) for a detailed assessment of the target system.
- You may need to run the script with `sudo` on certain systems (especially Linux or macOS) for certain scans (like SYN scans), as they may require root privileges.

### Troubleshooting
- If the script is not working as expected, ensure that:
  - Nmap is properly installed on your system and accessible from the command line.
  - You have sufficient privileges to perform certain types of scans (e.g., SYN scan).
  - The `nmap` module is installed using `pip`.

### Customization
- You can modify the port range in the script. Currently, it scans ports `1-1024`. You can change this range based on your needs.
- Additional Nmap flags and scan options can be added to the script for more advanced scanning features.

