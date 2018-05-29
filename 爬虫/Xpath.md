# Xpath解析
官方地址：https://www.w3.org/TR/xpath/all/

|表达式         |描述            |
| ------------- |:-------------:|
|nodename       |选取此节点的所有子节点
|/              |从当前节点选取直接子节点
|//             |从当前节点选取子孙节点
|.              |选取当前节点
|..             |选取当前节点的父节点
|@              |选取属性

eg:

    表达式
    //title[@lang='eng']
    / 或 //   加标签 标签匹配
    [@href="link4.html"] 标签的属性的匹配
    result = html.xpath('//a[@href="link4.html"]/../@class') 获取父类的class的值
    result = html.xpath('//a[@href="link4.html"]/parent::*/@class') 获取父类的class的值

    使用方式

    from lxml import etree
    
    所有节点
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//*')
    print(result)
    
    所有li节点
    from lxml import etree
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//li')
    print(result)
    print(result[0])

    所有li下的a节点
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//li/a')
    print(result)

