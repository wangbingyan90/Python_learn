import requests

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

url = "http://music.163.com/api/playlist/detail?id=37880978&updateTime=-1"

r = requests.get(url, headers=headers,timeout=30)

r.raise_for_status()

r.encoding = r.apparent_encoding

jsondata = r.json()

result = jsondata['result']

print('创建时间')
print(result['createTime'])

print('更新时间')
print(result['updateTime'])

print('播放次数')
print(result['playCount'])

print('封面')
print(result['coverImgUrl'])

print('介绍')
print(result['description'])

print('名称')
print(result['name'])

print('歌单')
print(result['id'])

print('介绍')
print(result['description'])

print('收藏次数')
print(result['subscribedCount'])

print('分享次数')
print(result['shareCount'])

print('评论次数')
print(result['commentCount'])

print('标签数组')
print(result['tags'])


