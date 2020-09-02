
import requests
from bs4 import BeautifulSoup
import lxml
import os
import urllib


urls = []

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


with open('url.txt', 'r') as f:
    url = f.readline()
    while url:
        urls.append(url)
        url = f.readline()
    f.close()


for url in urls:
    url = url[:-1]
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    title = soup.find('title').text[:10]
    imgs = soup.find_all('img')
    img_urls = []
    for img in imgs:
        img_url = img.get('src')
        img_urls.append(img_url)
    
    path = f'./images/{title}'
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


    for i, img_url in enumerate(img_urls):
        try:
            request = urllib.request.Request(img_url)
            response = urllib.request.urlopen(request)
            img = response.read()

            filename = f'{path}/{i}.jpeg'
            print(f'downlading ...{title} for {url} : NO.{i}')
            with open(filename, 'wb') as fi:
                #img = requests.get(url, headers=header(url)).content
                fi.write(img)
        except ValueError:
            continue
    

