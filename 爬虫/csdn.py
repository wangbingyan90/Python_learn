import requests
import re
import redis

def getHTMLText(url):
    '''
    获取网站源码
    '''
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("源码获取失败")
        return ""

def parsePage(html):
    '''
    分析页面，获取链接
    data：Url
    '''
    data = re.findall(r'<a strategy=\"new\" href=\"(.*?)\" t',html)
    return data

def parseArticle(data,r):
    '''
    分析文章获取标题,时间
    并直接存入数据库
    '''
    for url  in data:
        print(url)
        if(r.hexists("url",url)):
            continue
        r.hset("url",url,1)
        html = getHTMLText(url)
        add = re.findall(r'title-article\">(.*?)<.*?time\">(.*?)<',html,re.S)
        saveData(add[0],r)
    return 0

def saveData(add,r):
    id = r.incr("auto_id");
    r.set("data:" + str(id) + ":title",add[0])
    r.set("data:" + str(id) + ":time",add[1])
    print("id:"+ str(id) + "  插入数据："+ str(add))
    return 0

def actionE(url,r):
    html = getHTMLText(url)
    print(html)
    data = parsePage(html)
    parseArticle(data,r)


if __name__  == "__main__":
    url = "https://blog.csdn.net/nav/cloud"
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    # r.flushdb()
    actionE(url,r)
