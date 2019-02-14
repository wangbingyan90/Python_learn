# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['python123.io']

    # 方式一
    start_urls = ['http://python123.io/']

    # 方式二
    def start_requests(self):
        urls = [
            'http://python123.io/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        return super().start_requests()

    def parse(self, response):
        pass
