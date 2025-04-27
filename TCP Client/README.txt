The client creates a socket object using the socket.socket() method, specifying the IPv4 address family and the TCP socket type.

It then retrieves the hostname of the local machine using socket.gethostname().

The client attempts to connect to the server running on the local machine (localhost) using the specified port (444).

Once connected, it waits to receive a message from the server, with a buffer size of 1024 bytes.

After receiving the message, the client closes the socket connection.

Finally, the client decodes the message (which is received in byte format) into a string using ASCII encoding and prints the message to the console.