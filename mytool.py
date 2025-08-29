import os
import requests

# جلب القيم من Environment Variables
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TOKEN = os.getenv("TOKEN")  # إذا عندك Bot Token كمان

if not USERNAME or not PASSWORD:
    print("❌ USERNAME أو PASSWORD مو موجودين في Environment Variables")
    exit(1)

def login():
    print(f"[+] Logging in with USERNAME: {USERNAME} ...")
    
    # مثال (غيّر الرابط والداتا حسب الكود الأساسي تبعك)
    session = requests.Session()
    response = session.post("https://example.com/login", data={
        "username": USERNAME,
        "password": PASSWORD
    })

    if response.status_code == 200:
        print("✅ Login successful")
    else:
        print(f"❌ Login failed - Status code: {response.status_code}")

if __name__ == "__main__":
    login()
