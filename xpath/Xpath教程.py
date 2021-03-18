from lxml import etree
import requests

url = 'https://movie.douban.com/explore#!type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=20&page_start=0'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
re = requests.get(url,headers=headers).text
print(re)

tree = etree.HTML(re)
#print(tree)

result = tree.xpath('//div[@class="list"]//a/p/text()')
print(result)


#tbody标签是坑