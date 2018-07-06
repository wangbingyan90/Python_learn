import pymysql
import time

#
#wby 2018
#pip install pymysql
class sqlUtil:

    def __init__(self):
        self.db= pymysql.connect(host="localhost",user="root",password="root",db="wymusic",port=3306,charset="utf8")
        self.cursor = self.db.cursor()

    def __del__(self):
        super()
        self.db.close()

    def addPlayList(self,List_Id,List_Name,Author_Id,List_img,PlayCount):
        sql = "insert into Playlist(List_Id,List_Name,Author_Id,List_img,PlayCount)values(%d, '%s', %d, '%s',%d) " % (List_Id,List_Name,Author_Id,List_img,PlayCount)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            f = open('err.txt', 'a+',encoding='utf-8')
            f.write('数据保存失败：'+time.strftime("%Y-%m-%d %H:%M:%S")+sql+"\n")
            f.close()
            return ""


    def addhotPlaylist(self,List_Id):
        sql = "insert into hotPlaylist(id)values(%d) " % (List_Id)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            f = open('err.txt', 'a+',encoding='utf-8')
            f.write('数据保存失败：'+time.strftime("%Y-%m-%d %H:%M:%S")+sql+"\n")
            f.close()
            return ""
           


if __name__  == "__main__":
    api = sqlUtil()
    # api.addPlayList(1231,'aad',123,'qweqwe',12312)
    api.addhotPlaylist(11)