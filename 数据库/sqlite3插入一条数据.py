import sqlite3

connet = sqlite3.connect("test.db")
# 游标
cur = connet.cursor()
# 编写插入sql
sql = 'insert into t_person(pname,age) values(?,?)'

try:
    # 执行sql
    cur.execute(sql, ('张三', 24))
    # cur.executemany()
    # 提交事务
    connet.commit()
    print('成功')

except Exception as e:
    print(e)
    print("失败")
finally:
    cur.close()
    connet.close()
