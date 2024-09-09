#Jitong Zou
#CS5700
import socket
import sys

# Set up server address and port
HOST = "127.0.0.1" 
PORT = 65432 

# Retrieve command-line arguments
args = sys.argv
num = args[1] # Get the number passed to the script

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    # Connect to the server
    s.connect((HOST, PORT)) 
    # Send the number to the server, encoded to bytes
    s.sendall(num.encode())
    # Receive the response from the server, limited to 1024 bytes
    data = s.recv(1024) 
    # Print out what was sent and received
    print(f"Sent {num} and received {data!r}") #print to console