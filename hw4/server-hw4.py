from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import mimetypes

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve HTML or JSON content based on the requested resource
        file_type, _ = mimetypes.guess_type(self.path)
        if file_type == "text/html":
            try:
                with open(self.path, 'r') as file:
                    html = file.read()
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html")
                    self.end_headers()
                    self.wfile.write(html.encode("utf-8"))              
            except FileNotFoundError:
                self.send_error(404, message=f"File Not Found: {self.path}")
                self.send_header("Content-Type", "text/html;charset=utf-8")
                self.end_headers()
        elif file_type == "application/json":
            try:
                with open(self.path, 'r') as file:
                    json_data = file.read()
                    json_data = json.loads(json_data)
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(json_data).encode("utf-8")) 
            except FileNotFoundError:
                self.send_error(404, message=f"File Not Found: {self.path}")
                self.send_header("Content-Type", "text/html;charset=utf-8")
                self.end_headers()
        else:
            # Handle unsupported content type
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found - Unsupported Content Type") 

# Server setup
port = 8070
server_address = ('', port)
httpd = HTTPServer(server_address, MyHandler)

print(f"Serving on port {port}")
httpd.serve_forever()
