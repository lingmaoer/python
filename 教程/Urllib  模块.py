import urllib.request
'''
urllib.request.urlretrieve(网址，本地文件储存地址)   直接下载网页到本地
urllib.request.urlcleanup()   清除缓存
'''
#info()  看网页的信息
data = urllib.request.urlopen('https://blog.csdn.net/Key_book/article/details/80244033',timeout=5)
print(data.info())

#getcode()    网页抓取状态码
print(data.getcode())

#geturl()    获取当前访问的网页的url(页面)
print(data.geturl())

#超时设置
#timeout



































