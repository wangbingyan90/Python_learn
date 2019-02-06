# scrapy

学习scrapy

安装

    pip install scrapy

如：Scrapy安装错误：Microsoft Visual C++ 14.0 is required.

https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted

    pip install Twisted-17.5.0-cp36-cp36m-win_amd64.whl
    继续安装

主要依赖包
* lxml，一个高效的XML和HTML解析器
* parsel，一个写在lxml之上的HTML / XML数据提取库，
* w3lib，一个用于处理URL和网页编码的多用途帮助程序
* twisted，一个异步网络框架
* cryptography和pyOpenSSL，用于处理各种网络级安全需求


    https://docs.scrapy.org

创建项目

    scrapy startproject 项目名

主要解析方式：
    
    CSS选择器

    使用CSS和响应对象选择元素
    response.css('title')
    标题中提取文本
    response.css('title::text').extract()
    完整的title元素，包括其标签
    response.css('title').extract()
    只想要第一个结果(或以数字组)
    response.css('title::text').extract_first()
    正则表达式进行提取
    response.css('title::text').re(r'Quotes.*')

    XPath选择器

    response.xpath('//title')
    response.xpath('//title/text()').extract_first()


    分析函数
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }


