import pymysql

#创建链接
con = pymysql.connect(host = 'localhost',user="root",password='xieyuhao123',database='python_db',port=3306)
# print(con)
cur = con.cursor()
sql = "insert into t_student(sname,age,score) values (%s,%s,%s)"

try:
    cur.executemany(sql,[("小明",3,88),('小红',4,98),("小赵",3,60)])
    con.commit()
except Exception as e:
    print(e)
    con.rollback()
finally:
    con.close()