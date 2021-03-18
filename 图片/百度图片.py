import requests
import re

key = input('输入要查找的图片名字：')
page = eval(input("输入页数（一页30张）："))
for i in range(1, page + 1):
    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30&gsm=10000000000001e&1584950398904=".format(
        key, key, i * 30)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    res = requests.get(url, headers=headers).text
    # print(res)
    a = '"thumbURL":"(.*?)",'
    url_list = re.findall(a, res)
    # print(url_list)
    for ur in url_list:
        data = requests.get(ur, headers=headers).content
        # print(data)
        name = ur.split('/')[-1]
        with open('图片/' + name, 'wb')as f:
            f.write(data)
            print('图片{}下载完成'.format(name))
