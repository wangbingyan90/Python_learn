import requests
import re
import pymysql
 
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "失败2"
     
def parsePage(html):
    hrefs = re.findall(r'<a href=\"(.*?)\" title',html)
    titles = re.findall(r'title=\"(.*?)\" class=',html)
    imgs = re.findall(r'src=\"(.*?)\" /><span class',html)
    n = int(len(hrefs)-3)
    n = int(n/2)
    db = pymysql.connect(host="localhost",user="root",password="root",db="video",port=3306,charset="utf8")
    cursor = db.cursor()
    for i in range(n):
        p = i*2+4
        href = hrefs[p]
        title = titles[p-1]
        img = imgs[i]
        sql = "insert into video%d(time,href,title,img)values(%d, '%s', '%s', '%s')" % \
           (count,0, href ,title,img )
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("失败")
            db.rollback()
    db.close()
         
def main2():
    depth = 12
    start_url = 'http://j8508.com/wap/?m=vod-type-id-'+ str(count) + '-pg-'
    for i in range(depth):
        try:
            url = start_url + str(i+1) + '.html'
            html = getHTMLText(url)
            parsePage(html)
        except:
            continue
    print("完成")

count = int(5)
def main():
    global count
    for i in range(6):
        count = count + i
        main2()

main()
