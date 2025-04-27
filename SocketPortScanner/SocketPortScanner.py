import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 and TCP
s.settimeout(5)

host = input("Please enter the host's IP: ")

port = int(input("Enter a port: "))

def portScanner(port):
        
    if s.connect_ex((host, port)):
        print("The port is closed.")
    else:
        print("The port is open.")
        
portScanner(port)
