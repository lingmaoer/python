
import requests
from lxml import etree
import pprint

url = 'https://www.dytt8.net/html/gndy/dyzz/index.html'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}

response = requests.get(url,headers=headers)

#print(response)

html = response.content.decode('gbk','ignore')

#print(html)

etr = etree.HTML(html)

#print(etr)

movide_name = etr.xpath('//td[@height="26"]/b/a/text()')

#print(movide_name)

movides_url = etr.xpath('//td[@height="26"]/b/a/@href')

#print(movide_url)

for movide_url in movides_url:

    movide_url = 'https://www.dytt8.net'+movide_url

    #print(movide_url)

    res = requests.get(movide_url,headers=headers).content.decode('gbk','ignore')

    #pprint.pprint(res)

    etre = etree.HTML(res)

    name = etre.xpath('//p/text()')

    #print(name)

    for i in name[0:-8]:

        #print(i)

        with open("text.txt",'a+',encoding='utf-8')as f:

            f.write(i+'\n')














