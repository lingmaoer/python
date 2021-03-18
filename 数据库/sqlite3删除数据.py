import sqlite3

connet = sqlite3.connect("test.db")

cur = connet.cursor()

#创建查询sql
sql = 'delete from t_person where pon=?'

try:
    cur.execute(sql,(1,))
    connet.commit()

except Exception as e:
    print(e)
    connet.rollback()
finally:
    connet.close()