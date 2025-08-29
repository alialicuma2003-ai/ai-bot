import requests, os, re

r1 = requests.session()
imz = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    "cookie": "ig_did=0897491F-B736-4E7E-A657-37438D0967B8; csrftoken=xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe; rur=FTW; mid=XxTPfgALAAGHGReE-x_i1ISMG4Xr",
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.2 (Linux; Android 6.3; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
}

def login():
    global csrftoken, username, ds, sessionid

    login_url = 'https://www.instagram.com/accounts/login/ajax/'

    # بدال input() → نقرأ من Environment Variables
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    if not username or not password:
        print("❌ USERNAME أو PASSWORD مش متضبوطة في Environment Variables")
        return

    login_headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "ig_did=0897491F-B736-4E7E-A657-37438D0967B8; csrftoken=xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe; rur=FTW; mid=XxTPfgALAAGHGReE-x_i1ISMG4Xr",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/91.81 (Linux; Android 6.3; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36",
        "x-csrftoken": "xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe",
        "x-ig-app-id": "1217981644879628",
        "x-ig-www-claim": "0",
        "x-instagram-ajax": "180c154d218a",
        "x-requested-with": "XMLHttpRequest"
    }

    login_data = {
        "username": username,
        "enc_password": '#PWD_INSTAGRAM_BROWSER:0:&:' + password
    }

    def gooo_login():
        global csrftoken, sessionid, ds
        login_to_acc = r1.post(login_url, data=login_data, headers=login_headers)

        if 'userId' in login_to_acc.text:
            print("✅ Login Succeeded As @" + username + "\n")
            ds = login_to_acc.cookies['ds_user_id']
            csrftoken = login_to_acc.cookies['csrftoken']
            sessionid = login_to_acc.cookies['sessionid']
            print("[+] Sessionid : " + sessionid)
        else:
            print("❌ Login failed:", login_to_acc.text)

    gooo_login()

if __name__ == "__main__":
    login()
