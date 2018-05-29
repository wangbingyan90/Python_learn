import textUserMode


import requests
 
response = requests.get('https://www.12306.cn')
print(response.status_code)
'''
requests已经设置好了cookies
import requests
r = requests.get("https://blog.csdn.net/nav/cloud")
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)
'''

'''
http://httpbin.org 实用网站
import requests

data = {
    'name': 'germey',
    'age': 22
}
r = requests.get("http://httpbin.org/get", params=data)
print(r.json())

textUserMode.getHTMLText("http://httpbin.org")
'''



'''
调用浏览器
from selenium import webdriver

# browser = webdriver.Chrome()

# browser = webdriver.Firefox()

browser = webdriver.PhantomJS()
browser.get('https://www.baidu.com')
print(browser.current_url)

'''






'''
用于自提取headers
import requests
import re

response  = requests.get("https://blog.csdn.net")
# response  = requests.get("https://www.baidu.com")
s = response.headers['Set-Cookie']
print(s)
# s = 'uuid_tt_dd=10_37357874890-1527418193769-845989; Expires=Thu, 01 Jan 2025 00:00:00 GMT; Path=/; Domain=.csdn.net;, dc_session_id=10_1527418193769.963896; Expires=Thu, 01 Jan 2025 00:00:00 GMT; Path=/; Domain=.csdn.net;, uuid_tt_dd=5134527014351125271_20180527; expires=Wed, 24-May-2028 10:49:53 GMT; Max-Age=315360000; path=/; domain=csdn.net'
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
print(Cookie)
        

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
print(headers)
'''