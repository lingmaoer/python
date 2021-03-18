import sqlite3

connet = sqlite3.connect("test.db")

cur = connet.cursor()

#创建查询sql
sql = "select * from t_person"

try:
    cur.execute(sql)
    #获取结果集
    person = cur.fetchone()
    print(person)
except Exception as e:
    print(e)
finally:
    cur.close()
    connet.close()