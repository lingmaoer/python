import requests
import re

url = 'https://blog.csdn.net/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
data = requests.get(url,headers=headers).text
#print(data)
par1 = '<a href="(.*?)" target="_blank">'

rest_list1 = re.compile(par1).findall(data)
print(rest_list1)
'''
for rest in rest_list1:
    data1 = requests.get(rest,headers=headers).text
    #print (data1)
    par2 = '<h1 class="title-article">(.*?)</h1>'
    name = re.compile(par2).findall(data1)
    print (name)
    with open ('vide\\'+ name[0]+'.html','wb')as f:
        f.write(data1.encode())
'''
