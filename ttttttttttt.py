import you_get
import sys
import requests
import json
import threading
'''
path = './video'

url = 'https://www.bilibili.com/video/BV1Ji4y1878t'
'''
def download(path,url):
    sys.argv = ['you-set','-o',path,url]
    you_get.main()

def ExtractVide():
    url = ''
    headers = {cooki,user}
    response =  requests.get(url,headers=headers).text
    json_data = json.loads(response[37:-1])
    data = json_data['result']
    for i in data:
        arcurl = i['arcurl']
        path = './video'
        #download(path,arcurl)
        t = threading.Thread(target=download,args=(path,arcurl))
        t.start()
        t.join()




