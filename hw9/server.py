from socket import *
import sys

def get_server_ip():
    # Dynamically get the server's IP address
    hostname = gethostname()
    return gethostbyname(hostname)

def run_server(port):
    server_ip = get_server_ip()
    print(f"Server IP address: {server_ip}")
    print(f"Server port number: {port}")
    print("Ready to serve...")

    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((server_ip, port))
        s.listen()
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024).decode()

                if not data:
                    continue

                # Parse the incoming GET request
                request_line = data.split('\n')[0]
                if "GET" in request_line:
                    file_name = request_line.split()[1].strip('/')

                    # Attempt to open the file
                    try:
                        with open(file_name, 'r') as file:
                            file_content = file.read()
                        response = "Connection Successful!\n"
                        response += "---------------HTTP RESPONSE---------------\n"
                        response += "HTTP/1.1 200 OK\n"
                        response += file_content + "\n"
                        response += "---------------END OF HTTP RESPONSE---------------\n"
                    except FileNotFoundError:
                        response = "Connection Successful!\n"
                        response += "---------------HTTP RESPONSE---------------\n"
                        response += "HTTP/1.1 404 Not Found\n"
                        response += "---------------END OF HTTP RESPONSE---------------\n"
                else:
                    response = "Invalid Request!"

                conn.sendall(response.encode())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <PORT>")
        sys.exit(1)

    port = int(sys.argv[1])
    run_server(port)
