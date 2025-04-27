import socket 

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 444

clientsocket.connect((host, port)) # client connects to the server

message = clientsocket.recv(1024) #1024 is the buffer size

clientsocket.close()

print(clientsocket.decode('ascii')) #print the message