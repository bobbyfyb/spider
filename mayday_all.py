import json

from bs4 import BeautifulSoup
import requests
import xlwt
from selenium import webdriver

browser = webdriver.Chrome()
f = open('url.txt',"a")
a=0
for a in range(0,5):
    if a == 0:
        URL="http://569xe.com/569xe-tupianqu/TSE/"
    else:
        URL="http://569xe.com/569xe-tupianqu/TSE/index_"+str(a+1)+".html"
    browser.get(URL)
    html = browser.page_source
    soup = BeautifulSoup(html,'lxml')
    #print(soup)
    items = soup.find(class_='mod-col clearfix').find_all('li')
    #print(items)


    for item in items:
        try:
            url = 'http://569xe.com'+item.find('a').get('href')
            title = item.find('a').find('h2').string
            #print(title)
            if len(url)==42:
                f.write(url+'\n')
        except:
            continue
    print('第%s页已完成'%(a+1))
f.close()