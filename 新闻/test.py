# -*- encoding: utf-8 -*-
# @Time     :2020/11/3 9:19
# @Author   :ling_mao
# @File     :main.py
# @Software :PyCharm


import requests
import json

name_list = []
base_url = [""]
cookie = ''
# response = requests.get(base_url)
# print(response)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.111 Safari/537.36 ",
    'cookie': cookie
}
i = 1
for url in base_url:
    res = requests.get(url, headers=headers).text[16:-2:1]
    # print(res)
    # print(json.loads(res)['data']['photos'])
    photos = json.loads(res)['data']['photos']
    # print(photos[0])

    for photo in photos:
        # print(photo)

        name = photo['ownerName']
        # print(photo['ownerName'])
        # print(photo['ownerUin'])
        # print(photo['url'])
        data = requests.get(photo['url']).content
        # print(data)
        name_list.append(name)
        print(photo['ownerName'])
        with open('F:/绿协/种植统计表/第二次/' + str(i) + '-' + name + '.jpg', 'wb')as f:
            f.write(data)
        i += 1
name_list = set(name_list)
num = 1
for i in name_list:
    print(num, '\t', i)
    num += 1
