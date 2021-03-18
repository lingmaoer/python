# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import scrapy
from scrapy.pipelines.images import ImagesPipeline


class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_link = item['verticalSrc']
        yield scrapy.Request(image_link)
