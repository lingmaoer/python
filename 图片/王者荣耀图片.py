import requests
import json

base_url = 'https://pvp.qq.com/web201605/js/herolist.json'

response = requests.get(base_url)

txt = response.text

# print(txt)

tata_list = json.loads(txt)

# print(tata_list)

for i in tata_list:

    # print(i)

    ename = i['ename']

    cname = i['cname']

    try:

        skin_name = i['skin_name'].split('|')

    except Exception as e:

        print(e)

    # print(ename,cname,skin_name)

    for a in range(1, len(skin_name) + 1):
        url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(
            ename) + '-bigskin-' + str(a) + '.jpg'

        # print(url)

        data = requests.get(url).content

        with open("百度图片/" + cname + '-' + skin_name[a - 1] + '.jpg', 'wb')as f:
            f.write(data)

            print("图片：{}-{}下载完成".format(cname, skin_name[a - 1]))
