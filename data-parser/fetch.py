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

    url = f'https://grades.hs.ntnu.edu.tw/classtable/down.asp?sqlstr=15{cl}&type=class&selArrange=L&selWindow=Left'

    headers = {
        "Host": "grades.hs.ntnu.edu.tw",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Referer": "http://grades.hs.ntnu.edu.tw/classtable/top.asp",
        "Cookie": "selWindow=Left; selArrange=L; ASPSESSIONIDSSDQDDQC=BMJFDMPCNHEGGHHIGBEGOEED; ASPSESSIONIDSQDRCCQD=MMJHEDEDDMOBKDADKJFJDJAG",
        "Upgrade-Insecure-Requests": "1",
        "Sec-GPC": "1"
    }
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, 'html.parser')
    print(soup)
    sel = soup.select("body form table")

    print(sel)
    time.sleep(delay)


