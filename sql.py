import pymysql

db= pymysql.connect(host="localhost",user="root",password="root",db="video",port=3306,charset="utf8")
cursor = db.cursor()
sql = """INSERT INTO video6(time,href,title,img)
         VALUES (11, 'Mohan', 'asd', 'M')"""
sql_insert ="""insert into video5(time,href,title,img) values(4,'liu','1234','asdsda')"""

sqlq = "insert into video6(time,href,title,img)values(0, '/wap/?m=vod-play-id-865-src-1-num-1.html', '9- 無言妻 老公就在隔壁哦… 5', '/wap/upload/upload/20170608/20173516165368102.jpg')"

print(sqlq)
cursor.execute(sqlq)
db.commit()
db.close()
