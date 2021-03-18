import pymysql

#创建链接
con = pymysql.connect(host = 'localhost',user="root",password='xieyuhao123',database='python_db',port=3306)
# print(con)
cur = con.cursor()
sql = "select * from t_student"

try:
    cur.execute(sql)
    students = cur.fetchall()
    for student in students:
        print(student)
    con.commit()
except Exception as e:
    print(e)
    con.rollback()
finally:
    con.close()
'''
import pymysql

#创建链接
con = pymysql.connect(host = 'localhost',user="root",password='xieyuhao123',database='python_db',port=3306)
# print(con)
cur = con.cursor()
sql = "select * from t_student where age=3"

try:
    cur.execute(sql)
    students = cur.fetchall()
    for student in students:
        print(student)
    con.commit()
except Exception as e:
    print(e)
    con.rollback()
finally:
    con.close()
'''