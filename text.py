import textUserMode


import requests

'''
登陆成功
headers = {
    'Cookie':'q_c1=a15edffcb1344a36a36f44f53bdd084b|1525878546000|1525878546000; _zap=a807c53b-2440-4684-86ca-3415df302a69; d_c0="AJAju7Ommw2PTlih3DRVcE2ZMfk6yG1dJYI=|1526563873"; capsion_ticket="2|1:0|10:1527483449|14:capsion_ticket|44:NWUzZTBkZTkzOTMyNGFkMmIwNzI5NDMyYThiOTI0ZmU=|618b6840f229b0a79d19a97937759fea5d0669994d33fa19c89a38406346d753"; r_cap_id="OTVmMDNhNDYzYTQxNGEwY2E4MWIwMDRmY2UxNzAxMGM=|1527483456|3cbe272845688ed7151ede447cfff4bcef24d310"; cap_id="ZGM0NzI2MGU3YzI5NGIwNTgzOTMxOTc5MDMxMzhjMjc=|1527483456|7ca3c7afd477d4fd97bfbc7782c9712cc501d21f"; l_cap_id="OWI4OGMyMjNhZWVhNGZiZWFjOGYzMTJiMDk0NmE3ZjI=|1527483456|1b56f1081fb313f6559d4839ee13b844ec945562"; z_c0=Mi4xSUFvR0FnQUFBQUFBa0NPN3M2YWJEUmNBQUFCaEFsVk5WOXI0V3dDVTVGRlBwZFB3RllYNWk1bGp6NTl0WVE0MDdR|1527483479|317a61c41047a51ad3ba05ba396373759d74031d; __utmv=51854390.100--|2=registration_date=20150826=1^3=entry_date=20150826=1; __utma=51854390.218489189.1527483515.1527483515.1527495801.2; __utmz=51854390.1527495801.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _xsrf=fac89fa9-37e9-477f-a6b0-8330e3bb8711',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
r = requests.get('https://www.zhihu.com',headers=headers)
print(r.text)
'''




''' 
response = requests.get('https://www.12306.cn')
print(response.status_code)
'''

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