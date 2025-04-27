import socket

# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is the address family for IPv4, SOCK_STREAM is the socket type for TCP

host = socket.gethostname()
port = 444

serversocket.bind((host, port)) #bind to the port

serversocket.listen(3) #how many connections it can listen at one time


while True:
    clientsocket, address = serversocket.accept() #accept the connection

    print("Received connection from" % str(address))

    message = "Hello!Thank you for connnecting to the server!" + "\r\n"
    clientsocket.send(message.encode('ascii')) #send message to the client

    clientsocket.close()