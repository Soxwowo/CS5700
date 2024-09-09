#Jitong Zou
#CS5700

import socket

HOST = "127.0.0.1" #Standard loopback interface address (localhost)
PORT = 65432 #Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #Create a new socket using the given address family,
    # socket type, and protocol number
    s.bind((HOST, PORT)) #Bind the socket to an address and port number. The socket must not already be bound.
    s.listen() #Enable a server to accept connections.
    conn, addr = s.accept() #Accept a connection. The socket must be bound to an address and listening for connections.
    #The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on
    #the connection, and address is the address bound to the socket on the other end of the connection.
    with conn: #with keyword is used for unmanaged resources such as socket stream or file stream, used for exception
        #handling
        while True: #looping the input stream to receive all byte data from the client
            data = conn.recv(1024) #receives the data from the client
            if not data:
                break #breaks out once no more data to receive
            data = int(data) + 100
            conn.sendall(str(data).encode()) #send the data back to the client (echo it back). The socket must be connected to a remote
            #socket (client's socket).