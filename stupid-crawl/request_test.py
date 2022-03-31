from bs4 import BeautifulSoup
import requests
import time
import os

classtable_baseurl = "http://grades.hs.ntnu.edu.tw/classtable/"

table_index_page = requests.get(classtable_baseurl)
cookies_name = table_index_page.headers['Set-cookie'].split(';')[0].split('=')[0]

print('請輸入 '+ cookies_name +' ,並保持該頁面開啟...')
session_id = input(cookies_name + '=')

classtable_baseurl = "http://grades.hs.ntnu.edu.tw/classtable/"
#table_index_page = requests.get(classtable_baseurl)
#cookies = dict(ASPSESSIONIDAQCSTTQS = table_index_page.headers['Set-cookie'].split(';')[0].split('=')[1])
cookies = dict({(cookies_name , session_id)})
top_req = requests.get(classtable_baseurl + 'top.asp', cookies=cookies)
if len(top_req.text) < 1500:  #所回傳的回應短到應該不是課表
    print('所輸入的 '+ cookies_name +' 很可能是錯的，請檢查後再試')
    exit()
top_parse = BeautifulSoup(top_req.text, 'html.parser')

s1_list = [(i.attrs['value'], i.contents[0])
           for i in top_parse.find(id='s1').contents
           if ((i.name == 'option') and str.isnumeric(i.attrs['value']))]
for i in s1_list:
    table = requests.get(classtable_baseurl + 'down.asp?sqlstr=' + str(i[0]) +
                         '&type=class&selArrange=L&selWindow=Right',
                         cookies=cookies)
    if len(table.text) < 1500:  #所回傳的回應短到應該不是課表
        print('所輸入的 '+ cookies_name +' 很可能是錯的，請檢查後再試')
        exit()
    table_file = open('./tables/s1/' + str(i[1]) + '.html',
                      mode='w',
                      encoding='utf-8')
    print(str(i))
    table_file.write(table.text)
    table_file.close()
    time.sleep(0.1)

print('班級資料抓取完畢')
input('繼續抓取？')

s2_list = [(i.attrs['value'], i.contents[0])
           for i in top_parse.find(id='s2').contents
           if ((i.name == 'option') and str.isnumeric(i.attrs['value']))]
for i in s2_list:
    table = requests.get(classtable_baseurl + 'down.asp?sqlstr=' + str(i[0]) +
                         '&type=teacher&selArrange=L&selWindow=Right',
                         cookies=cookies)
    if len(table.text) < 1500:  #所回傳的回應短到應該不是課表
        print('所輸入的 '+ cookies_name +' 很可能是錯的，請檢查後再試')
        exit()
    table_file = open('./tables/s2/' + str(i[1]) + '.html',
                      mode='w',
                      encoding='utf-8')
    print(str(i))
    table_file.write(table.text)
    table_file.close()
    time.sleep(0.1)

print('教師資料抓取完畢')
input('繼續抓取？')

s3_list = [(i.attrs['value'], i.contents[0])
           for i in top_parse.find(id='s3').contents
           if ((i.name == 'option') and str.isnumeric(i.attrs['value']))]
for i in s3_list:
    table = requests.get(classtable_baseurl + 'down.asp?sqlstr=' + str(i[0]) +
                         '&type=room&selArrange=L&selWindow=Right',
                         cookies=cookies)
    if len(table.text) < 1500:  #所回傳的回應短到應該不是課表
        print('所輸入的 '+ cookies_name +' 很可能是錯的，請檢查後再試')
        exit()
    table_file = open('./tables/s3/' + str(i[1]) + '.html',
                      mode='w',
                      encoding='utf-8')
    print(str(i))
    table_file.write(table.text)
    table_file.close()
    time.sleep(0.1)

print('教室資料抓取完畢')

print('資料抓取完畢')
