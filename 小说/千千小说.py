import requests
import parsel

url = 'https://www.qqxs.cc/xs/115/115569/'  # 更换网址改变小说
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}


def txt(url):  # 获取章节内容
    response = requests.get(url, headers=headers)
    # print(response.content.decode('gbk'))
    obj = parsel.Selector(response.content.decode('gbk'))
    name1 = obj.css('div.zhangjieming>h1::text').get()
    # print(name1)
    name1 = '\n' + name1
    texts = obj.css('div.zhangjieTXT::text').getall()
    # print(text)
    book_text = [name1]
    for i in texts:
        # print(i.strip())
        book_text.append(i.rstrip())
    book_text.pop(1)
    for i in book_text:
        with open(book_name + '.txt', 'a+', encoding='utf-8')as f:
            f.write(i)
    print(f"下载完成{name1}")


def book(url):  # 获取书的章节
    # url = 'https://www.qqxs.cc/xs/115/115569/'
    res = requests.get(url, headers=headers)
    # print(res.content.decode('gbk'))
    select = parsel.Selector(res.content.decode('gbk'))
    url2 = select.css("dl>dd>a::attr(href)").getall()
    # print(url2)
    # name = select.css("dl>dd>a::text").getall()
    # print(name)
    global book_name
    book_name = select.css("div#info>h1::text").get()
    # print(book_name)
    for j in url2:
        url3 = url + j
        # print(url3)
        txt(url3)


book(url)
