# scrapy

学习scrapy

学习的最佳方式是使用示例 见p1

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

执行项目

    进入项目目录
    scrapy crawl 项目名
    或 scrapy crawl 项目名 -o quotes.jl

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

##### 命令参数使用

这些参数传递给Spider的__init__方法，默​​认情况下变为spider属性

    -a参数
    scrapy crawl quotes -o quotes-humor.json -a tag=humor
    为参数提供的值tag将通过self.tag。您可以使用此选项使您的蜘蛛只获取具有特定标记的引号，并根据参数构建URL
    如果您将tag=humor参数传递给此蜘蛛，您会注意到它只会访问humor标记中的URL ，例如 http://quotes.toscrape.com/tag/humor。
    更多参数：https://docs.scrapy.org/en/latest/topics/spiders.html#spiderargs

进一步学习

移步基础学习




