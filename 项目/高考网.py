import parsel
import requests
from pyecharts import options
from pyecharts.charts import Bar


def get_data():
    url = 'http://www.gaokao.com/henan/fsx/'
    res = requests.get(url).content.decode("gbk")
    # print (res)
    html = parsel.Selector(res)
    # print(html)
    years = html.xpath("//table//tr[@class='wkTit']/th[@width='72']/text()").getall()[0:11]
    # print(years)
    ybs1 = html.xpath('//table//tr[@class="c_blue"]/td/text()').getall()
    ybs2 = []
    for yb in ybs1:
        ybs2.append(yb.strip())
    # print(ybs2)
    wkyb = ybs2[1:12]
    lkyb = ybs2[13:24]
    # print(wkyb,lkyb)

    ebs1 = html.xpath('//table//tr[@class="c_white"]/td/text()').getall()
    # print(ebs1)
    ebs2 = []
    for eb in ebs1:
        ebs2.append(eb.strip())
    # print(ebs2)
    wkeb = ebs2[1:12]
    wkzk = ebs2[13:24]
    # print(wkeb,wkzk)

    lkeb = ebs2[25:36]
    lkzk = ebs2[37:48]
    # print(lkeb,lkzk)
    return years, wkyb, lkyb, wkeb, wkzk, lkeb, lkzk


def see(years, wkyb, lkyb, wkeb, wkzk, lkeb, lkzk):
    c = Bar()
    c.add_xaxis(years)
    c.add_yaxis("文科一本", wkyb)
    c.add_yaxis("文科二本", wkeb)
    c.add_yaxis("文科专科", wkzk)
    c.add_yaxis("理科一本", lkyb)
    c.add_yaxis("理科二本", lkeb)
    c.add_yaxis("理科专科", lkzk)
    c.set_global_opts(title_opts=options.TitleOpts(title='河南历年高考分数线', subtitle="2009-2019"))
    c.render('河南历年高考分数统计图.html')
    print("成功")


years, wkyb, lkyb, wkeb, wkzk, lkeb, lkzk = get_data()
# print(years,wkyb,lkyb,wkeb,wkzk,lkeb,lkzk)
see(years, wkyb, lkyb, wkeb, wkzk, lkeb, lkzk)

'''
c=Bar()#生成条形图
#添加x,y轴
c.add_xaxis()
c.add_yaxis("文科一本",zhi)
c.add_yaxis("文科二本",zhi)
#添加标题和副标题
c.set_global_opts(title_opts=options.TitleOpts(title=diqiname+'历年高考分数线',subtitle="2009-2019"))
#命名
c.render(diquname+'历年高考分数统计图.html')#渲染数据，自动生成HTML文件
'''
