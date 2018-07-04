import requests

# url = ' http://music.163.com/api/search/get/web'
url = 'http://music.163.com/discover/playlist'
# url = 'http://music.163.com/discover/playlist/?cat=古风&order=hot'
# url = 'http://music.163.com/discover/playlist/?order=hot&cat=全部&limit=35&offset=35'

headers = {
    'Host': 'music.163.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'JSESSIONID-WYYY=5dC%2F%2FQVEU%5C7XWrP%5CDyq0DSMlhAH5I7jCXt1UGXj%2BARUIvuTyFH3XU%5Cr3mY2Nupmnz3Ru5NVEGQd7SGIUkWSs6WHCzBaMnwoAPMdh8f0HJZSdeJ%2BkhDEbkPripDgAHTeYTaf1GSMwm1trRequBnAy06gz9tEAM4dQHijY2bWNDfXpUMZY%3A1530512499413; _iuqxldmzr_=32; _ntes_nnid=25a0db38f67e4f3efa8aeec1d8a63926,1530510699431; _ntes_nuid=25a0db38f67e4f3efa8aeec1d8a63926; __utma=94650624.1721149033.1530510700.1530510700.1530510700.1; __utmb=94650624.8.10.1530510700; __utmc=94650624; __utmz=94650624.1530510700.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_TID=NXO5cPZfmFiloDyPnyZJ56NT4CeNLyTa',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0, no-cache',
    'Pragma': 'no-cache'
    }
data = {
    's': '电影',
    'type': '1000',
    'offset': '0',
    'total': 'true',
    'limit': '60'
}
params = {
        "order": "hot",
        "cat": u"古风",
        "limit": 35,
        "offset": 35
    }
# r = requests.get("http://music.163.com/discover/playlist/", params=params)
# r = requests.post(url,data=data)
# r = requests.post("http://music.163.com/weapi/v1/resource/comments/R_SO_4_293940?csrf_token=19d102d38c0693f9e0271b18696477f4", headers=headers,timeout=30)

r = requests.get(url,headers=headers,timeout=30)

f = open('test.txt', 'w',encoding='utf-8')

f.write(r.text)
f.close()