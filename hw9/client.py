# Jitong Zou
# CS5700
# Homework 9-Web Server
from socket import *
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python client.py <server_ip> <port> <filename>")
        sys.exit(1)

    # Get command line arguments
    server_ip = sys.argv[1]
    port = int(sys.argv[2])
    filename = sys.argv[3]

    client_socket = socket(AF_INET, SOCK_STREAM)
    
    # Set timeout (e.g., 5 seconds)
    client_socket.settimeout(5)

    try:
        # Attempt to connect to the server and send the request
        client_socket.connect((server_ip, port))
        client_socket.send(f"GET {filename} HTTP/1.1\r\n\r\n".encode())
        
        # Receive and print the complete response from the server
        response = ""
        while True:
            part = client_socket.recv(1024).decode()
            if not part:
                break
            response += part
        print(response)
    except (ConnectionRefusedError, timeout):
        # Print error message if connection fails or times out
        print("\n\nError while connecting!")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
