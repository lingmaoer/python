import requests
import parsel

base_url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E7%BE%8E%E5%A5%B3%E5%90%A7&fr=search'
#print(base_url)
headers = {"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36"}

response = requests.get(base_url,headers = headers).text()
#print(response)

html = parsel.Selector(response)
title_url = html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@herf').extract()#取数据

second_url = 'https://tieba.baidu.com'
for url in title_url:
    all_url = second_url+url
    #print(all_url)

    respond_2 = requests.get(all_url,headers=headers)
    respond_2_data = parsel.Selector(respond_2)
    result_list = respond_2_data.xpath("//cc/div/img[@class='BED_Image']/@src").extract()

    for li in result_list:
        img_data = requests.get(result_list,headers=headers).content()

        file_name=li.split('/')[-1]
        with open('vide/'+file_name,'wb')as f:
            f.write(img_data)
            print(file_name+'下载完成')



