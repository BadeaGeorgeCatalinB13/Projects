import nmap

scanner = nmap.PortScanner()

print("Welcome")
print("-------")

ip_address = input("Please enter the IP address you want to scan: ")
print("The IP address you entered is :"  + ip_address)

type(ip_address)

resp = input("""\n
            1.SYN ACK SCAN(TCP)
            2.UDP SCAN
            3.Comprehensive scan\n""")

print("You selected a valid option " + resp)

if resp == "1":
    print("Scanner Version", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS', sudo=True)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_address].state()) # IP Address Up or Down
    print(scanner[ip_address].all_protocols())
    print("Aici este raspunsul: ", scanner[ip_address]['tcp'])
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())
elif resp == "2":
    print("Scanner Version", scanner.nmap_version)
    scanner.scan(ip_address, '1-1024', '-v -sU', sudo=True)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_address].state()) # IP Address Up or Down
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['udp'].keys())
elif resp == "3":
    print("Scanner Version", scanner.nmap_version)
    scanner.scan(ip_address, '1-1024', '-v -sS -sV -sC -A -O', sudo=True)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_address].state()) # IP Address Up or Down
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())
