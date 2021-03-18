import pymysql

#创建链接
con = pymysql.connect(host = 'localhost',user="root",password='xieyuhao123',database='python_db',port=3306)
# print(con)
cur = con.cursor()
sql = "update t_student set score=%s where sno=%s"

try:
    cur.execute(sql,(88,1))
    con.commit()
except Exception as e:
    print(e)
    con.rollback()
finally:
    con.close()