import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
for j in range(1, 128):
    url = 'https://api.bilibili.com/pgc/season/index/result?season_version=-1&area=-1&is_finish=-1&copyright=-1' \
          '&season_status=1&season_month=-1&pub_date=-1&style_id=-1&order=4&st=1&sort=0&page={' \
          '}&year=-1&season_type=1&pagesize=20&type=1'.format(j)
    result = requests.get(url, headers=headers)
    # print(result.text)
    txts = json.loads(result.text)
    # print(txts["data"]['list'])
    for i in txts['data']['list']:
        #     # print(i)
        if i['badge'] == "限时免费":
            print(i['link'], i['title'])
            # y = input("是否下载(y是)")
            # if y == "y":
            #     xiazai.fun(i['link'])
