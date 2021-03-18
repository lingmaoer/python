#浏览器伪装
import urllib.request

url = "http://blog.net"
head = ("Urser-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363")
opener = urllib.request.build_opener()
opener.addheaders = [head]
data = opener.open(url).read()
print(data)
'''with open ('BLOG.txt','w',encoding='utf-8') as f:
    f.write(data.decode('utf-8','ignore'))
'''


