#HTTP  自动模拟    get
#  .html?字段=值&字段=值

import urllib.request
import re
#get 请求实践--实现百度信息自动搜索-----
'''
keywd ='Python'
#keywd = urllib.request.quote(keywd)
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
url = 'http://www.baidu.com/s?wd='+keywd
data = urllib.request.urlopen(url).read().decode('utf-8')
print(data)
pat = 'title":(.*?),'
rest = re.compile(pat).findall(data)
print(rest)
'''

#POST  请求
'''
import urllib.parse
posturl = "http://iqianyue.com/mypost/"
postdata = urllib.parse.urlencode({"name":"43534322","pass":"1223443",}).encode('utf-8')
#Request(真实地址,)
req = urllib.request.Request(posturl,postdata)
rest = urllib.request.urlopen(req).read().decode('utf-8')
print(rest)
'''






