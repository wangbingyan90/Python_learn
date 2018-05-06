import requests
import redis

def getJson(url):
    '''
    获取接口数据
    '''
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.json()
    except:
        print("数据获取失败")
        return ""


def actionOne(url,r):
    jsonData = getJson(url)
    print(type(jsonData['articles'][0][url]))

if __name__  == "__main__":
    url = "https://blog.csdn.net/api/articles?type=new&category=cloud"
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    # r.flushdb()
    actionOne(url,r)


