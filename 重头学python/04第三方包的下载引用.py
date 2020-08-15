import pymysql


db=pymysql.connect(host="127.0.0.1",user="root",password="root",db="wm")
cur=db.cursor()
try:
    cur.execute("select * from student;")
    res=cur.fetchall()
    print(res)
except:
    print("sql语句写错了")

#第一次用python操作数据库  哇哇哇哇 查询数据库wm下叫wm的表 哇  2020-08-14

#pip install 包名