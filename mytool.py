import requests 
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
    global csrftoken , username 
    global ds 
    global sessionid 
    login_url = 'https://www.instagram.com/accounts/login/ajax/' 
    def vc(): 
        global username,password 
        username = input("[+] Username @l7xn : ") 
        password = input("[+] Password #Darkn12345 : ") 
    vc() 
    login_headers = { 
        "accept": "*/*", 
        "accept-encoding": "gzip, deflate, br", 
        "accept-language": "en-US,en;q=0.9", 
        "content-length": "267", 
        "content-type": "application/x-www-form-urlencoded", 
        "cookie": "ig_did=0897491F-B736-4E7E-A657-37438D0967B8; csrftoken=xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe; rur=FTW; mid=XxTPfgALAAGHGReE-x_i1ISMG4Xr", 
        "origin": "https://www.instagram.com", 
        "referer": "https://www.instagram.com/", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-origin", 
        "user-agent": F"Mozilla/91.81 (Linux; Android 6.3; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36", 
        "x-csrftoken": "xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe", 
        "x-ig-app-id": "1217981644879628", 
        "x-ig-www-claim": "0", 
        "x-instagram-ajax": "180c154d218a", 
        "x-requested-with": "XMLHttpRequest"} 
    login_data = { 
        "username": username, 
        "enc_password": '#PWD_INSTAGRAM_BROWSER:0:&:' + password} 
    def gooo_login(): 
        global ig_did, csrftoken, sessionid 
        login_to_acc = r1.post(login_url, data=login_data, headers=login_headers) 
        if 'To secure your account' in login_to_acc.text: 
            print("Check Your Password And Try Again")
            print(" instagram @l7xm ") 
            print(" thank you ")
            return login() 
        if login_to_acc.content == b'{"user": false, "authenticated": false, "status": "ok"}': 
            print("Check Your Username And Try Again") 
            print(" instagram @l7xn ") 
            print(" thank you ")
            return login() 
        elif ('showAccountRecoveryModal') in login_to_acc.text: 
            print("Check Yo Password And Try Again") 
            print(" instagram @syee ") 
            print(" thank you ")
            return login() 
        elif ('{"message": "checkpoint_required"') in login_to_acc.text: 
            print("Checkpoint") 
            print("[1] Close Swap") 
            print("[2] Try Again") 
            print("[3] Send Code To (Email-Phone_Number)") 
            ch = input("[ 1-2-3 ] : ") 
            if ch == '1': 
                quit() 
            elif ch == '2': 
                return gooo_login() 
            elif ch == '3': 
                uuu = login_to_acc.json() 
                iiii = uuu['checkpoint_url'] 
                oooo = 'https://www.instagram.com'+iiii+'?__a=1' 
                llll = r1.get(oooo,headers=imz).text 
            try: 
                s_email = re.findall('"email":"(.*?)"', llll) 
                print(F'[1] Email : {s_email}') 
                s_phone = re.findall('"phone_number":"(.*?)"', llll) 
                print('[2] Phone_Number : '+s_email) 
            except: 
                pass 
            mmm = input('Send To( 1 Email ~ 2 Phone_Number ) :') 
            if mmm == '1': 
                Se_Email = r1.post(oooo, headers=login_headers, data={ 
                    'choice': '1' 
                }, cookies=login_to_acc.cookies) 
                if 'sent to the email address' in Se_Email.text:print("Sent To Email") 
            elif mmm == '2': 
                Se_Emawil = r1.post(oooo, headers=login_headers, data={ 
                    'choice': '0' 
                }, cookies=login_to_acc.cookies) 
                print(Se_Emawil.text) 
            AsA = input("Security_Code : ") 
            yfd = r1.post(oooo, headers=login_headers, data={ 
                'security_code': F'{AsA}' 
            }, cookies=login_to_acc.cookies) 
            if '"status": "ok"' in yfd.text: 
                gooo_login() 
            else: 
                print("[!] Error") 
                print(" Accpect the Secure ")
                print(" instagran @l7xn ")
                print( " Thank you " )
                quit() 
        elif 'userId' in login_to_acc.text: 
            print("Login Succeeded As @"+username+"\n") 
            ds = login_to_acc.cookies['ds_user_id'] 
            csrftoken = login_to_acc.cookies['csrftoken'] 
            sessionid = login_to_acc.cookies['sessionid'] 
            print("[+] Sessionid : "+sessionid) 
            print("""
░██████╗██╗░░░██╗███████╗███████╗
██╔════╝╚██╗░██╔╝██╔════╝██╔════╝
╚█████╗░░╚████╔╝░█████╗░░█████╗░░
░╚═══██╗░░╚██╔╝░░██╔══╝░░██╔══╝░░
██████╔╝░░░██║░░░███████╗███████╗
╚═════╝░░░░╚═╝░░░╚══════╝╚══════╝""")

            print(" ⠀ ⠀   ⠀ ⠀   ⠀ ⠀   ⠀ ⠀   ⠀ ⠀   ⠀ ⠀   ⠀ ⠀   ⠀  ⠀ ⠀   ⠀ ⠀   ⠀ ⠀   ⠀ ⠀   ⠀ ⠀   ⠀ ⠀   ⠀ ⠀   ⠀ ⠀   ⠀ ⠀   ⠀")
            print(" instagram : @l7xn ")
            print(" Follow Me <3 " )
            print(" Thank You " )
        else: 
            print(login_to_acc.text) 
            quit() 
    gooo_login() 
login()
