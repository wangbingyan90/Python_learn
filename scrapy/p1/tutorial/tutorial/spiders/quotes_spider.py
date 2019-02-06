import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # 保存页面 命令 scrapy crawl quotes
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        # 选择并保存输出内容 
        # 命令 scrapy crawl quotes -o quotes.json 两次独立表头
        # 命令 scrapy crawl quotes -o quotes.jl  两次同一表头
        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').extract_first(),
        #         'author': quote.css('small.author::text').extract_first(),
        #         'tags': quote.css('div.tags a.tag::text').extract(),
        #     }


        # urljoin()方法构建完整的绝对URL （因为链接可以是相对的）并向下一页生成新请求，将自身注册为回调来处理下一页的数据提取并保持爬网遍历所有页面。
        # 当你在回调方法中产生一个Request时，Scrapy会安排发送该请求并注册一个回调方法，以便在该请求完成时执行。
        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').extract_first(),
        #         'author': quote.css('small.author::text').extract_first(),
        #         'tags': quote.css('div.tags a.tag::text').extract(),
        #     }
        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)


        # 创建请求的快捷方式 response.follow：与scrapy.Request不同
        # 它response.follow直接支持相对URL无需调用urljoin。
        # 注意，response.follow只返回一个Request实例; 你仍然需要提出这个请求。
        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').extract_first(),
        #         'author': quote.css('span small::text').extract_first(),
        #         'tags': quote.css('div.tags a.tag::text').extract(),
        #     }
        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

        # 也可以传递选择器response.follow而不是字符串; 此选择器应提取必要的属性：
        # for href in response.css('li.next a::attr(href)'):
        #     yield response.follow(href, callback=self.parse)

        # 对于<a>元素，有一个快捷方式：response.follow自动使用其href属性。
        # 所以代码可以进一步缩短：
        # response.follow(response.css('li.next a'))无效是因为 response.css返回一个类似于列表的对象，
        # for a in response.css('li.next a'):
        #     yield response.follow(a, callback=self.parse)

