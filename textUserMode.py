import requests

def getHTMLText(url):
    '''
    获取网站源码
    '''
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
        return r.text
    except:
        print("源码获取失败")
        return ""