import urllib.request
import re

url = "https://news.china.com/social/1007/20200319/37942695.html"
data = urllib.request.urlopen(url).read().decode('utf-8')
#print(data)
pat = "<p>([^用].*?)</p>|</span>(.*?)</p>"
rest = re.compile(pat).findall(data)
for i in rest:
    print(i[0])








