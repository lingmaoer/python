import sqlite3

connet = sqlite3.connect("test.db")

cur = connet.cursor()

#创建查询sql
sql = 'update t_person set pname=? where pon=?'

try:
    cur.execute(sql,("小嗨",2))
    connet.commit()

except Exception as e:
    print(e)
    connet.rollback()
finally:
    connet.close()