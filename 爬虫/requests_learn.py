import requests

response  = requests.get("https://www.baidu.com")
print(type(response)) # <class 'requests.models.Response'>
print(response.status_code) # 200

print(type(response.text)) # context \xe7
print(response.content)

response.enconding = "utf-8"
print(response.text) # 中文输出
print(response.content.decode("utf-8"))

print(response.cookies) # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
print(response.headers)
'''
第一次请求时的响应参数：
{'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 所有缓存机制
 'Connection': 'Keep-Alive',  连接
 'Content-Encoding': 'gzip',
 'Content-Type': 'text/html', 
 'Date': 'Sat, 26 May 2018 13:40:52 GMT',
 'Last-Modified': 'Mon, 23 Jan 2017 13:23:56 GMT', 
 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18',
 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'
}
'''
 


