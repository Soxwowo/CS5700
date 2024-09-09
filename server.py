#Jitong Zou
#CS5700
import socket

# Set up server address and port
HOST = "127.0.0.1" 
PORT = 65432 

#Create a new socket using the given address family,
#socket type, and protocol number
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    #Bind the socket to an address and port number.
    s.bind((HOST, PORT)) 
    #Enable a server to accept connections.
    s.listen() 
    conn, addr = s.accept() #
    #with keyword is used for unmanaged resources such as socket stream or file stream, used for exception handling
    with conn: 
        while True: 
            data = conn.recv(1024) #receives the data from the client
            if not data:
                break #breaks out once no more data to receive
            data = int(data) + 100
            conn.sendall(str(data).encode()) #send the data back to the client. The socket must be connected to a remote socket (client's socket).