import requests
import re
import time

respose=requests.get('http://www.youxiake.net/gallery?f=&q=%E4%BA%BA%E5%83%8F').text
time.sleep(1)
pat=r'img src="(http://img4.youxiake.com/.*?imageView2/2/w/1200)" '

urls=re.findall(pat,respose)
#print(urls)

for url in urls:
    file_name = url.split('/')[-1]
    response = requests.get(url)
    with open('图片','wb')as f:
        f.write(response.content)
