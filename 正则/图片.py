import requests
import re

url = 'https://www.vmgirls.com/fresh'
headers ={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36'}
res = requests.get(url,headers=headers)
#print(res)
data = res.text
#print(data)
par = '<a href="(.*?)" class="list-title text-md h-2x" target="_blank">'
url_list = re.compile(par).findall(data)
#print(url_list)
for url1 in url_list:
    resp = requests.get(url1,headers=headers).text
    #print(resp)
    par1 = '<p><a href="(.*?)"'
    url_1 = re.compile(par1).findall(resp)
    #print(url1)
    for url2 in url_1:
        name = url2.split('/')[-1]
        data1 = requests.get(url1,headers=headers).content
        with open('vide/'+name,'wb')as f:
            f.write(data1)
            print('%s:下载完成'%name)