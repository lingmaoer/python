import requests
import parsel

url = 'http://www.gaokao.com/henan/fsx/'
res = requests.get (url).content.decode ("gbk")
# print (res)
html=parsel.Selector(res)
# print(html)
years=html.xpath("//table//tr[@class='wkTit']/th[@width='72']/text()").getall()[0:11]
# print(years)
ybs1=html.xpath('//table//tr[@class="c_blue"]/td/text()').getall()
ybs2=[]
for yb in ybs1:
    ybs2.append(yb.strip())
# print(ybs2)
wkyb=ybs2[1:12]
lkyb=ybs2[13:24]
# print(wkyb,lkyb)

ebs1 = html.xpath ('//table//tr[@class="c_white"]/td/text()').getall ()
# print(ebs1)
ebs2=[]
for eb in ebs1:
    ebs2.append(eb.strip())
# print(ebs2)
wkeb=ebs2[1:12]
wkzk=ebs2[13:24]
# print(wkeb,wkzk)

lkeb=ebs2[25:36]
lkzk=ebs2[37:48]
# print(lkeb,lkzk)