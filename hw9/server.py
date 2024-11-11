# Jitong Zou
# CS5700
# Homework 9-Web Server
from socket import *
import sys

def handle_client(connection_socket, requested_file):
    # Message of successful connection
    connection_socket.send("\nConnection Successful!\n\n\n".encode())

    # Attempt to read the content of the requested HTML file
    try:
        with open(requested_file, 'r') as file:
            content = file.read()
            response = "\nHTTP/1.1 200 OK\n\n\n\n" + content + "\n"
    except FileNotFoundError:
        response = "\nHTTP/1.1 404 Not Found\n\n\n\n"

    # Send HTTP response in the specified format
    connection_socket.send("---------------HTTP RESPONSE---------------\n".encode())
    connection_socket.send(response.encode())
    connection_socket.send("---------------END OF HTTP RESPONSE---------------\n".encode())

def main():
    if len(sys.argv) != 2:
        print("Usage: python server.py <port>")
        sys.exit(1)

    # Get port number
    port = int(sys.argv[1])
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)

    # Dynamically obtain server IP address
    server_ip = gethostbyname(gethostname())
    print(f"server IP address: {server_ip}")
    print(f"server port number: {port}\n\n")
    print("Ready to serve...")

    # Loop waiting for client connection
    while True:
        connection_socket, addr = server_socket.accept()
        try:
            # Receive and parse requests, obtain file names
            request = connection_socket.recv(1024).decode()
            requested_file = request.split()[1]  
            handle_client(connection_socket, requested_file)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            connection_socket.close()

if __name__ == "__main__":
    main()

