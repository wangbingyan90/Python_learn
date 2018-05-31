import requests


# 对象化请求
from requests import Request, Session
url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)


# requests还提供了其他认证方式 pip3 install requests_oauthlib
'''
使用OAuth1认证 https://requests-oauthlib.readthedocs.io/en/latest/
from requests_oauthlib import OAuth1
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
              'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)
'''


# 身份认证 
from requests.auth import HTTPBasicAuth
r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
r = requests.get('http://localhost:5000', auth=('username', 'password'))
print(r.status_code)


# 设置代理
proxies = {
  # 普通用法
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",

  # 使用HTTP Basic Auth
  "http": "http://user:password@10.10.1.10:3128/",

  # requests还支持SOCKS协议的代理 安装socks pip3 install 'requests[socks]'
  'http': 'socks5://user:password@host:port',
  'https': 'socks5://user:password@host:port'
}
# 超时时间秒 timeout设置为None，或者不设置直接留空，永久等待，timeout=(5,11, 30) 传入元组：求总和
requests.get("https://www.taobao.com", proxies=proxies,timeout = 1) 


# SSL证书验证 自动验证
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)


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

# 上传文件
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
 


