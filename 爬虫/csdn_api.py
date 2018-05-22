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


def getHTMLText(url):
    '''
    获取网站源码
    url：网站地址
    '''
    headers = {
        'Host': 'blog.csdn.net',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://blog.csdn.net/nav/cloud',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Tingyun-Id': 'wl4EtIR_7Is;r=976669768',
        'Cookie': 'uuid_tt_dd=4099473511411770564_20180522; dc_session_id=10_1526976401745.516297; TY_SESSION_ID=44a0e163-9d87-49c1-8a47-8cb70dbb5695; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1526976641; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1526976651; ADHOC_MEMBERSHIP_CLIENT_ID1.0=80021b53-245d-2f0a-9e86-a5c831756bf7; dc_tos=p94eq2',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
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
    id = r.incr("auto_id");
    r.set("data:" + str(id) + ":title",add[0])
    r.set("data:" + str(id) + ":time",add[1])
    print("id:"+ str(id) + "  插入数据："+ str(add))
    return 0


def parseArticle(data,r):
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
        html = getHTMLText(url)
        add = re.findall(r'title-article\">(.*?)<.*?time\">(.*?)<',html,re.S)
        if len(add)==0:
            continue
        saveData(add[0],r)
    return 0



def actionOne(r):  
    url = "https://blog.csdn.net/api/articles?type=new&category=cloud"
    headers = {
        'Host': 'blog.csdn.net',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://blog.csdn.net/nav/cloud',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Tingyun-Id': 'wl4EtIR_7Is;r=976669768',
        'Cookie': 'uuid_tt_dd=4099473511411770564_20180522; dc_session_id=10_1526976401745.516297; TY_SESSION_ID=44a0e163-9d87-49c1-8a47-8cb70dbb5695; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1526976641; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1526976651; ADHOC_MEMBERSHIP_CLIENT_ID1.0=80021b53-245d-2f0a-9e86-a5c831756bf7; dc_tos=p94eq2',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    jsonData = getJson(url,headers)
    parseArticle(jsonData['articles'],r)


if __name__  == "__main__":
    
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    # r.flushdb()
    while 1:
        actionOne(r)
  


