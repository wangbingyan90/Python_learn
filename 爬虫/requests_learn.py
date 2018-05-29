import requests


# requests会话
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)


'''
# requests手动设置cookies
cookies = 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000; d_c0="AGDAs254kAqPTr6NW1U3XTLFzKhMPQ6H_nc=|1474273938"; __utmv=51854390.100-1|2=registration_date=20130902=1^3=entry_date=20130902=1;a_t="2.0AACAfbwdAAAXAAAAso0QWAAAgH28HQAAAGDAs254kAoXAAAAYQJVTQ4FCVgA360us8BAklzLYNEHUd6kmHtRQX5a6hiZxKCynnycerLQ3gIkoJLOCQ==";z_c0=Mi4wQUFDQWZid2RBQUFBWU1DemJuaVFDaGNBQUFCaEFsVk5EZ1VKV0FEZnJTNnp3RUNTWE10ZzBRZFIzcVNZZTFGQmZn|1474887858|64b4d4234a21de774c42c837fe0b672fdb5763b0'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get("http://www.zhihu.com", cookies=jar, headers=headers)
print(r.text)
'''

# requests自动设置cookies
r = requests.get("https://www.baidu.com")
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)

# 上传图片
files = {'file': open('favicon.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)

# 下载图片
r = requests.get("https://github.com/favicon.ico")
with open('favicon.ico', 'wb') as f:
    f.write(r.content)

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
 


