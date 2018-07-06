'''
网易云音乐 Api
'''
from bs4 import BeautifulSoup
import requests
from multiprocessing.pool import Pool
# import time
# from sqlUtil import sqlUtil

class Api:

    def __init__(self):
        self.headers = {
            'Host': 'music.163.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0, no-cache',
            'Pragma': 'no-cache'
        }
        self.cookies = {
            'appver': '1.5.2'
        }
        self.timeout = 30
        # self.f = open('err.txt', 'a+',encoding='utf-8')
        # self.sqlconnet = sqlUtil()


    # 网络请求
    def httpRequest(self, url,type=None):
        try:
            print("获取页面")
            r = requests.get(url, headers=self.headers,timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            if type=='text':
                return r.text
            else:
                return r.json()
        except:
            # self.f.write('数据获取失败：'+time.strftime("%Y-%m-%d %H:%M:%S")+url+"\n")
            # self.f.close()
            return ""


    #解析歌单列表
    def parsePlayList(self,html):
        soup = BeautifulSoup(html, 'lxml')
        list_pic = soup.select('ul#m-pl-container li div img')
        list_nameUrl = soup.select('ul#m-pl-container li div a.msk')
        list_num = soup.select('div.bottom span.nb')
        list_author = soup.select('ul#m-pl-container li p a')
        n = 0
        length = len(list_pic)
        while n < length:
            print('歌单图片：'+list_pic[n]['src']+'\n\n')
            print('歌单名称：'+list_nameUrl[n]['title']+'\n\n歌单地址：'+list_nameUrl[n]['href']+'\n\n')
            print('歌单播放量：'+list_num[n].text+'\n\n')
            print('歌单作者：'+list_author[n]['title']+'\n\n作者主页：'+list_author[n]['href']+'\n\n\n')
            n += 1

    def hotPlayListmain(self,offset):
        print("启动线程")
        for n in range(offset-6,offset):
            url='http://music.163.com/discover/playlist?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset='+str(n*35)
            self.parsePlayList(self.httpRequest(url,'text'))

    def getHotPlayList(self,limit=None,offset=None):
        if limit==None :
            print("开始爬取")
            groups = ([x * 6 for x in range(1, 7)])
            pool = Pool()
            print("Pool")
            pool.map(self.hotPlayListmain, groups)
            pool.close()
            pool.join()
        else:
            url='http://music.163.com/discover/playlist?order=hot&cat=%E5%85%A8%E9%83%A8&limit='+str(limit)+'&offset='+str(offset)
            self.parsePlayList(self.httpRequest(url,'text'))

    def text(self):
        # self.sqlconnet.addPlayList(12313213,'aad',123,'qweqwe',12312)
        url='http://music.163.com/discover/playlist?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
        self.parsePlayList(self.httpRequest(url,'text'))

if __name__  == "__main__":
    api = Api()
    api.getHotPlayList()

