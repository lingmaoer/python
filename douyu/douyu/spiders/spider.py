import json

import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['https://www.douyu.com']
    base_url = 'https: //m.douyu.com/api/room/list?page={}&type=yz'
    offset = 0
    start_urls = [base_url.format(offset)]

    def parse(self, response):
        # 提取数据
        data_list = json.loads(response, body)['data']
        if len(data_list['list']) == 0:
            return
        for data in data_list['list']:
            item = DouyuItem
            print(item)
            item['nickname'] = data['nickname'].encode("utf-8")
            item['verticalSrc'] = data['verticalSrc']

            yield item
        self.offset += 1
        url = self.base_url.format(self.offset)

        yield scrapy
