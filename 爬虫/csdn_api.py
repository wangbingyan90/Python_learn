import requests
import redis
import re

def getJson(url,headers):
    '''
    获取接口数据
    url：接口地址
    '''
    try:
        r = requests.get(url, headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.json()
    except:
        print("数据获取失败")
        return ""


def getHTMLText(url,headers):
    '''
    获取网站源码
    url：网站地址
    '''
    try:
        r = requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("源码获取失败")
        return ""


def saveData(add,r):
    '''
    数据存入redis数据数据库
    '''
    # id = r.incr("auto_id");
    # r.set("data:" + str(id) + ":title",add[0])
    # r.set("data:" + str(id) + ":time",add[1])
    i = r.llen('data')
    r.lpush('data',add[0])
    print("id:"+ str(i) + "  插入数据："+ str(add))
    return 0


def parseArticle(data,r,headers):
    '''
    分析文章获取标题,时间
    并直接存入数据库
    '''
    for articleInfo  in data:
        url = articleInfo["url"]
        # print(url)
        if(r.hexists("url",url)):
            continue
        r.hset("url",url,1)
        html = getHTMLText(url,headers)
        add = re.findall(r'title-article\">(.*?)<.*?time\">(.*?)<',html,re.S)
        if len(add)==0:
            continue
        saveData(add[0],r)
    return 0



def actionOne(r,headers):  
    url = "https://blog.csdn.net/api/articles?type=new&category=cloud"
    jsonData = getJson(url,headers)
    parseArticle(jsonData['articles'],r,headers)

def getHeaders():
    response  = requests.get("https://blog.csdn.net")
    s = response.headers['Set-Cookie']
    Cookie = str()
    uuid_tt_dd = ''
    dc_session_id = ''
    for add in s.split(';'):
        addone = add.split('=')
        if(addone[0]=='uuid_tt_dd'):
            uuid_tt_dd = addone[1]
        if(addone[0]==', dc_session_id'):
            dc_session_id = addone[1]
        Cookie = 'uuid_tt_dd='+uuid_tt_dd+'; dc_session_id='+dc_session_id+';'
        headers = {
            'Host': 'blog.csdn.net',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://blog.csdn.net/nav/cloud',
            'Cookie': Cookie,
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
    return headers

if __name__  == "__main__":
    headers = getHeaders()
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    # r.flushdb()
    while 1:
        actionOne(r,headers)
  


