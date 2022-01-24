import requests
import time 
import random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

delay_coices = [8, 5, 10, 6, 20, 11]
for i in range(4, 82):
    # Create a fake user agent
    user_agent = UserAgent()
    delay = random.choice(delay_coices)
    cl = 0
    if i >= 10:
        cl = i
    else:
        cl = "0" + str(i)

    url = f'http://grades.hs.ntnu.edu.tw/classtable/down.asp?sqlstr=15{cl}&type=class&selArrange=L&selWindow=Left'

    headers = {
        "Host": "grades.hs.ntnu.edu.tw",
        "User-Agent": user_agent.random,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://duckduckgo.com/",
        "Connection": "keep-alive",
        "Cookie": "selWindow=Left; selArrange=L; ASPSESSIONIDSSDQDDQC=BMJFDMPCNHEGGHHIGBEGOEED",
        "Upgrade-Insecure-Requests": "1",
        "Sec-GPC": "1",
        "Cache-Control": "max-age=0"
    }
    resp = requests.get(url , headers=headers)

    soup = BeautifulSoup(resp.text, 'html.parser')

    sel = soup.select("body form table")

    print(sel)
    time.sleep(delay)
string =[sel]
Alist = []
Blist = []

string = string.split('<td class="tdColumn">')
for i in range(6):
    string.pop(i)
string = string.split('<td class="tdColumn">')
for i in range(1, 69, 2):
    string.pop(i)
for i in range(35):
    tin = string[i]
    tin = tin.split("(</span>)")
    for i in range(2):
        tina = tin[i]
        tina = tina.split(">")
        tinal = tina[2]
        tinal = tinal[:4]
        Alist.append(tinal)
    for i in range(2):
        tina = tin[i]
        tina = tina.split(">")
        tinal = tina[2]
 
