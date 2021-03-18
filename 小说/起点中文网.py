import requests
import parsel
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    'Cookie': '_qda_uuid=271846ea-1e8d-138e-90b0-f93198bffec3; e2=%7B%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A14%7D; e1=%7B%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22qd_G55%22%2C%22l1%22%3A14%7D; _csrfToken=AgdBdWxl8oNkjnuZHLuQSzYRTd8ig5gwmVieLiXL; newstatisticUUID=1585397588_752891972; qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; pgv_pvi=1588572160; e1=%7B%22pid%22%3A%22qd_P_limitfree%22%2C%22eid%22%3A%22qd_E05%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_free%22%2C%22eid%22%3A%22%22%7D; lrbc=1017627763%7C512601902%7C0%2C1018027842%7C526514164%7C1%2C1115277%7C22058859%7C0; rcr=1017627763%2C1018027842%2C1115277',
    'Host': 'book.qidian.com',
    'Referer': 'https://book.qidian.com/info/1017627763'

}
# url = 'https://read.qidian.com/chapter/eh2Vm8l0RbDbhZU9AFSCzA2/7DKtweBjI3dp4rPq4Fd4KQ2'
url = 'https://book.qidian.com/info/1017627763#Catalog'

res = requests.get(url, headers=headers).text
# print(res)
etr = etree.HTML(res)
# tit = etr.xpath('//ul[@class="cf"]/li/a/text()')#章节名
# print(tit)
tit_books = etr.xpath("//ul[@class='cf']/li/a/@href")  # 章节地址
# print(tit_book)
for titles in tit_books:
    title = 'https:' + titles
    # print(title)
    response = requests.get(title, headers=headers)
    print(response.text)
    obj = parsel.Selector(response.text)

    title1 = obj.css('h3.j_chamterName>span::text').get()  # 章节名
    print(title1)
    texts = obj.css('div.read-content.j_readContent>p>span::text').getall()  # 内容
    print(texts)
    # books_name = obj.css('div.book-cover-wrap>h1::text').get()
    # print(books_name)
    title_text = [title1]
    for i in texts:
        # print(i)
        title_text.append(i)
    for j in title_text:
        with open(title1 + '.txt', 'a+')as f:
            f.write(j + '\n')
    print(f"{title1}下载完成")
