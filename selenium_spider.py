import os
import urllib

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


browser = webdriver.Chrome()
browser.get("http://569xe.com/569xe-tttppp/1401430.html")
html = browser.page_source
soup = BeautifulSoup(html,'lxml')
#print(soup)

items = soup.find(class_='main-content').find_all('img')
url_list=[]
for item in items:
    picture_url = item.get('src')
    if len(picture_url) < 60:
        url_list.append(picture_url)

    #print(picture_url)

def header(referer):

    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }

    return headers

for url in url_list:
    j=1
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    get_img = response.read()
    with open('D:/Python/pachong/day_04/picture/'+str(j)+'.jpg','wb') as fp:
        fp.write(get_img)
        print('第%s张图片下载完成' %(j))
    j+=1