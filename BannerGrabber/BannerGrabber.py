import socket

def BannerGrabber(ip_address, port):

    s = socket.socket()
    s.connect((ip_address, int(port)))
    s.settimeout((5))
    print(s.recv(1024))

def main():

    ip_address = input("Please enter the IP: ")
    port = str(input("Please enter the port: "))
    BannerGrabber(ip_address, port)

main()
