import pymysql

#创建链接
con = pymysql.connect(host = 'localhost',user="root",password='xieyuhao123',database='python_db',port=3306)
# print(con)
cur = con.cursor()
sql = """
    create table t_student(
     sno int primary key auto_increment,
     sname varchar(30) not null,
     age int(2),
     score float(3,1))"""

try:
    cur.execute(sql)
except Exception as e:
    print(e)
finally:
    con.close()
