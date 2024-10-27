from socket import *
import sys

def run_client(server_ip, port, file_name):
    try:
        with socket(AF_INET, SOCK_STREAM) as s:
            # Set a timeout for the connection attempt (e.g., 5 seconds)
            s.settimeout(5)
            s.connect((server_ip, port))

            # Send HTTP GET request
            request = f"GET /{file_name} HTTP/1.1\n"
            s.sendall(request.encode())

            # Receive and print the server response
            response = s.recv(4096).decode()
            if response:
                print(response)
            else:
                print("Error while connecting!")
    except (ConnectionRefusedError, timeout, gaierror):
        print("Error while connecting!")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python client.py <SERVER_IP> <PORT> <HTML_FILE_NAME>")
        sys.exit(1)

    server_ip = sys.argv[1]
    port = int(sys.argv[2])
    file_name = sys.argv[3]

    run_client(server_ip, port, file_name)
