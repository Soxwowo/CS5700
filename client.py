#Jitong Zou
#CS5700

import socket
import sys

HOST = "127.0.0.1" #The server's host name or IP address
PORT = 65432 #The port used by the server

args = sys.argv
num = args[1]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #Create a new socket using teh given address famiily, socket
    #type and protocol number
    s.connect((HOST, PORT)) #Connect to a remote socket at the address and port
    #is byte
    data = s.recv(1024) #Receive data from the socket. The return type is a bytes object representing the data received.
    #The maximum amount of data to be received in each chunk is 1024 as specified.
    print(f"Sent {num} and received {data!r}") #print to console