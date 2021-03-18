import requests

headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/83.0.4103.14 Safari/537.36 Edg/83.0.478.13"}
def get_id():
    base_url="https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
    response=requests.get(base_url,headers=headers).json()
    #print(response)
    heros=response['hero']
    for hero in heros:
        #print(hero)
        heroId=hero['heroId']
        url=f'https://game.gtimg.cn/images/lol/act/img/js/hero/{heroId}.js'
        response=requests.get(url,headers=headers).json()
        # print(response)
        skins=response['skins']
        #print(skins)
        for skin in skins:
            # print(skin)
            mainImg=skin['mainImg']
            #print(mainImg)
            if mainImg:
                skin_name = skin['name']
                heroTitle = skin['heroTitle']
                try:
                    with open("图片/"+heroTitle+'-'+skin_name+'.jpg','wb')as f:
                        f.write(requests.get(mainImg).content)
                        print(heroTitle+'-'+skin_name,"下载完成")
                except Exception as e:
                    print(e)
get_id()