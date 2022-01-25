import urllib.request as req
import requests
from bs4 import BeautifulSoup
class_name=1550
class_html = {}
while class_name<1582:
    
    url="https://grades.hs.ntnu.edu.tw/classtable/down.asp?sqlstr="+str(class_name)+"&type=class&selArrange=L&selWindow=Right"
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"})
    with req.urlopen(request) as response:
        data=response.read().decode("big5")
    class_name+=1
    class_html[data]=int(class_name)
print(class_html)
##能抓html，但會斷線
