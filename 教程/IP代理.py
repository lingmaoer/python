'''
import urllib.request


ip = '5.228.45.32:808'
proxy = urllib.request.ProxyHandler({'http':ip})
#print(proxy)
opener=urllib.request.build_opener(proxy,urllib.request.ProxyHandler)
urllib.request.install_opener(opener)


url = 'https://baidu.com'
urllib.request.urlopen(url).read().decode('utf-8','ignore')


#ip 代理池
import random
import urllib.request
ippoois = [
    '',
    '',
    '',
    ]
def ip (ip):
    thisip = random.choices(ip)
    proxy = urllib.request.ProxyHandler ({'http': thisip})
    # print(proxy)
    opener = urllib.request.build_opener (proxy, urllib.request.ProxyHandler)
    urllib.request.install_opener (opener)


#ip 代理池2（接口不稳定）异常处理
def ip ():
    thisall=urllib.request.urlopen("网站").read().decode("utf-8")
    ippools=[]
    for iteam in thisall:
        thisiplist = iteam.decode('utf-8','ignore')
        ippools.append(thisiplist)
    thisip = ippools
    proxy = urllib.request.ProxyHandler ({'http': thisip})
    # print(proxy)
    opener = urllib.request.build_opener (proxy, urllib.request.ProxyHandler)
    urllib.request.install_opener (opener)

'''
import urllib.request
import requests
urllib.request.ProxyHandler({"http":"ip:post"})

proxy = {
    'http':'       :  '
}
#不信任网站
#verify = False







