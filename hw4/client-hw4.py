import http.client
import sys

def get_resource(resource):
    '''
    Insert your code here.    


    '''
    # Create a connection to the server
    conn = http.client.HTTPConnection('localhost', 8070)

    # Send a GET request for the resource
    # 发送GET请求
    if resource.endswith(".html"):
        headers = {"Content-Type": "text/html"}
    elif resource.endswith(".json"):
        headers = {"Content-Type": "application/json"}
    else:
        headers = {"Content-Type": ""}

    conn.request("GET", resource, headers=headers)

    # Get the response from the server
    response = conn.getresponse()

    # Extract status code, content type, and content
    status_code = response.status
    content_type = response.getheader('Content-Type')
    content = response.read().decode()

    print(f"Response Status Code: {status_code}")
    print(f"Content Type: {content_type}")
    print("Response Content:")
    print(content)

    conn.close()

get_resource(sys.argv[1])