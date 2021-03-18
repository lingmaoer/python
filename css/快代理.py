import requests
import parsel

for j in range(1,11):
    url =f'https://www.kuaidaili.com/free/inha/{j}'

    response=requests.get(url).text
    # print(response)
    html=parsel.Selector(response)

    ips=html.css("table.table.table-bordered.table-striped>tbody>tr>td[data-title='IP']::text").extract()
    # for ip in ips:
    #     print(ip)

    ports=html.css("table.table.table-bordered.table-striped>tbody>tr>td[data-title='PORT']::text").extract()
    # # for port in ports:
    # #     print(port)
    #
    types = html.css("table.table.table-bordered.table-striped>tbody>tr>td[data-title='类型']::text").extract()
    # # for type in types:
    # #     print(type)

    #ip_list=[]
    for i in zip(types,ips,ports):
        # ip={}
        # ip1=i[1]+':'+i[2]
        with open("123.csv","a",encoding='utf-8')as f:
            f.write(f"{i[0]},{i[1]},{i[2]}\n")
        # ip[f"{i[0]}"]=ip1
        # ip_list.append(ip)
    # # print(ip_list)
    # for io in ip_list:
    #     res=requests.get("https://www.baidu.com/",proxies=io)
    #     print(res.status_code)
