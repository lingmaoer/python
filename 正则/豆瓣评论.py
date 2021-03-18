import requests
import re

c=1
for a in range(0,5):
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=20&page_start={}'.format(a*20)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    respon = requests.get(url,headers=headers).text
    #print(respon)
    na = '"title":"(.*?)",'
    name_list = re.compile(na).findall(respon)
    #print(name)
    url_re = '"url":"(.*?)",'
    url_list = re.compile(url_re).findall(respon)
    #print(url_list)
    for i in range(0,20):
        #print(name[i],url_list[i])
        url1 = (url_list[i]+'reviews').split('\\')
        name = name_list[i]
        #print(url1)
        for b in range(0,5):
            url2 = (url1[0]+url1[1]+url1[2]+url1[3]+url1[4]+url1[5])+"?start={}".format(b*20)
            #print(url2)
            res = requests.get(url2,headers=headers).text
            #print(res)
            url_res = '<h2><a href="(.*?)">'
            url3 = re.compile(url_res).findall(res)
            #print(url3)
            for j in url3:
                #print(j)
                res2 = requests.get(j,headers = headers).text
                data = '<p>(.*?)</p>'
                txt = re.compile(data).findall(res2)
                print(txt)
                if txt != []:
                    for k in txt:
                        #print(k)
                        with open ("评论/"+name+'.txt','a+',encoding='utf-8')as f:
                            f.write(k+'\n')