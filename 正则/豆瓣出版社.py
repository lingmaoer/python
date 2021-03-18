import urllib.request
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
url = 'https://read.douban.com/provider/all'
data = urllib.request.Request(url,headers=headers)
data = urllib.request.urlopen(data).read().decode('utf-8')
#print(data)
pat = '<div class="name">(.*?)</div>'
rest = re.compile(pat).findall(data)
#print(rest)
with open("出版社.txt",'a+',encoding='utf-8') as f:
    for book in rest:
        f.write(book+'\n')
