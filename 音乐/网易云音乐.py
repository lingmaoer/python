import requests

url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
data = {
    'params': 'UPHstMxJJQYJbD8UHQTOAvAMpuCjR0TgFm8sh5W2Vz0T01N3EMIrFFtQbW4j+NA6XaW74lNQYOL41oalyq7BEtvCYT92EuSOwwBsb7UAK1iaLH18L6sS6HmN+xQU/Xqa77dtIj9rzHhyT2dVHuEyOfIBlPRK4D5yvwN1mvay1pOAX6S20nLpXPdBZv7fCWuENhnWg5AwNxYrED9QWTmbmX2daTanUQ/dP5BZu6L8Jq5f34rUb2kf7oOKfGfAAyqBehiiaQZNorXUuFKT72eX+cW8fHJhLUIz6f2mF37FTRU=',
    'encSecKey': '267cac6739541ce34503da48068397c65a0a7d922655bf61a164f5dc2941a649a4b886235592f458868eeff377442d501ebc1a1fd28384499213426f5685e06cf585f561a899fed10385fb58768d48e722921d84db0489fed7a19acb9d8869163a8b4e322bc3635048c2c3585078270d1b9ca748a9cc664e248b65f93ab5417d'
}
response = requests.post(url, data=data).json()
# print(response)
id_list = response['result']['songs']
for id in id_list:
    # print(id)
    url_list = []
    iteam = {}
    iteam['id'] = id['id']
    iteam['name'] = id['name']
    url_list.append(iteam)
    # print(url_list)
    url_music = 'http://music.163.com/song/media/outer/url?id=' + str(id['id']) + '.mp3'
    # print(url_music)
    res = requests.get(url_music).content
    # print(data1)
    with open('vide/' + id["name"] + ".mp3", 'wb')as f:
        f.write(res)
        print('下载完成：{}'.format(id['name']))
