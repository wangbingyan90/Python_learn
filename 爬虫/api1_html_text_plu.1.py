import requests

url = 'https://blog.csdn.net/nav/cloud'

headers = {
    'Connection':"keep-alive",
    'Accept':"application/json",
    'X-Requested-With':"XMLHttpRequest",
    'User-Agent':"Mozilla/5.0 (Linux; Android 6.0.1; C106 Build/ZAXCNFN5801712291S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.2623.91 Mobile Safari/537.36 Html5Plus/1.0",
    'Content-Type':"application/json",
    'Accept-Encoding':"gzip, deflate",
    'Accept-Language':"zh-CN,en-US;q=0.8"
    }

# url = 'http://www.baidu.com'

r = requests.get(url,headers=headers,timeout=30)
r.raise_for_status()
r.encoding = r.apparent_encoding
# print(r.json())

print(type(r.json()))