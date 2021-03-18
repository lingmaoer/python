import sqlite3

#创建链接
con = sqlite3.connect("test.db")
# print(con)

#创建游标对象
cur = con.cursor()

#编写创建表的sql语句
sql ='create table t_person(' \
     'pon INTEGER primary key autoincrement,' \
     'pname VARCHAR not null ,' \
     'age INTEGER ' \
     ')'

try:
    #执行sql语句
    cur.execute(sql)
    print('创建成功')
except Exception as e:
    print(e)
    print("创建失败")
finally:
    #关闭游标
    cur.close()
    #关闭连接
    con.close()