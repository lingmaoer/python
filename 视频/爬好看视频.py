import requests
import json

bast_url='https://haokan.baidu.com/videoui/api/videorec?tab=dongman&act=pcFeed&pd=pc&num=20&shuaxin_id=1584628096322'
#headers = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
base_url = 'https://haokan.baidu.com/videoui/api/videorec?tab=dongman&act=pcFeed&pd=pc&num=20&shuaxin_id=1584628096322'
response = requests.get (base_url, headers=headers)
data = response.text

json_data = json.loads (data)
data_list = json_data['data']['response']['videos']
for data1 in data_list:
    video_title = data1["title"] + '.mp4'
    video_url = data1["play_url"]
    void_data = requests.get (video_url, headers=headers).content
    with open ('vide\\' + video_title, 'wb') as f:
        f.write (void_data)
        print (data1['title'] + '-------下载完成-----')


