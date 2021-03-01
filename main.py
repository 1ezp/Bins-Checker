import requests,time
from fake_useragent import UserAgent


ua=UserAgent()
slp = int(input("Sleep: "))
r = requests.Session()
def check(bin):

    url = f"https://lookup.binlist.net/{bin}"

    headers = {
        "Accept-Version": "3",
        'User-Agent':ua.random
    }

    respone = r.get(url,headers = headers)
    try:
        if respone.json()['type'] == 'debit' and respone.json()['prepaid'] == True:
            print('[+] '+bin)
            with open('good.txt','a') as add:
                add.write(str(bin)+"\n")
            time.sleep(slp)
        else:
            print('[-] ' + bin)
            time.sleep(slp)
    except:
        print('[-] '+bin+":"+str(respone.status_code))
        time.sleep(slp)
for bin in open('bins.txt','r').read().splitlines():
    check(bin)