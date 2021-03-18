import requests
import parsel

for j in range(1,11):
    url =f'https://www.kuaidaili.com/free/inha/{j}/'

    response=requests.get(url).text
    # print(response)
    html=parsel.Selector(response)

    ips=html.xpath("//table[@class='table table-bordered table-striped']/tbody/tr/td[@data-title='IP']/text()").getall()
    # for ip in ips:
    #     print(ip)

    ports=html.xpath("//table[@class='table table-bordered table-striped']/tbody/tr/td[@data-title='PORT']/text()").getall()
    # for port in ports:
    #     print(port)

    types = html.xpath("//table[@class='table table-bordered table-striped']/tbody/tr/td[@data-title='类型']/text()").getall()
    # for type in types:
    #     print(type)
    ip_list=[]
    for i in zip(types,ips,ports):
        ip={}
        ip1=i[1]+':'+i[2]
        ip[f"{i[0]}"]=ip1
        ip_list.append(ip)
    # print(ip_list)
    for io in ip_list:
        res=requests.get("https://www.baidu.com/",proxies=io)
        print(res.status_code)




# import requests
# from lxml import etree
#
# for j in range(1,6):
#     url =f'https://www.kuaidaili.com/free/inha/{str(j)}/'
#
#     response=requests.get(url).text
#     #print(response)
#     html=etree.HTML(response)
#     ips=html.xpath("//table[@class='table table-bordered table-striped']/tbody/tr/td[@data-title='IP']/text()")
#     for ip in ips:
#         print(ip)
#
#     ports=html.xpath("//table[@class='table table-bordered table-striped']/tbody/tr/td[@data-title='PORT']/text()")
#     for port in ports:
#         print(port)
#
#     types = html.xpath("//table[@class='table table-bordered table-striped']/tbody/tr/td[@data-title='类型']/text()")
#     for type in types:
#         print(type)
#     ip_list=[]
#     for i in zip(types,ips,ports):
#         ip={}
#         ip1=i[1]+':'+i[2]
#         ip[f"{i[0]}"]=ip1
#         print(ip)
#         ip_list.append(ip)
#
#     print(ip_list)
#     for io in ip_list:
#         res=requests.get("https://www.baidu.com/",proxies=io)
#         print(res.status_code)