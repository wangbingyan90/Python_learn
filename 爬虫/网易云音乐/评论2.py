import requests
import json

headers = {
    'Cookie': 'appver=1.5.0.75771',
    'Referer': 'http://music.163.com',
}
# 为了方便，这里直接使用AES加密过后的用户名密码数据
# 跟截图不一样，无所谓了
user_data = {
    'params': 'vRlMDmFsdQgApSPW3Fuh93jGTi/ZN2hZ2MhdqMB503TZaIWYWujKWM4hAJnKoPdV7vMXi5GZX6iOa1aljfQwxnKsNT+5/uJKuxosmdhdBQxvX/uwXSOVdT+0RFcnSPtv',
    'encSecKey': '46fddcef9ca665289ff5a8888aa2d3b0490e94ccffe48332eca2d2a775ee932624afea7e95f321d8565fd9101a8fbc5a9cadbe07daa61a27d18e4eb214ff83ad301255722b154f3c1dd1364570c60e3f003e15515de7c6ede0ca6ca255e8e39788c2f72877f64bc68d29fac51d33103c181cad6b0a297fe13cd55aa67333e3e5'
}
song_id = 420513460
url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_%s/?csrf_token=' % (song_id,)
r = requests.post(url, headers=headers, data=user_data)
if r.status_code == 200 and r.text.find('comments') != -1:
    last_comments = json.loads(r.text)['comments']
    total_comments = json.loads(r.text)['total']
    print(last_comments)  # 太长，不贴了
    print(total_comments)  # 69