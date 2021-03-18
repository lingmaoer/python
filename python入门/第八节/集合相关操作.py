s = {10, 20, 30, 40, 50, 60}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)

# 一次添加一个
s.add(80)
print(s)

# 一次添加多个
s.update({200, 400, 600})
print(s)
s.update((100, 200))
s.update([300, 500, 700])
print(s)

print('-----------删除操作-------------')
# 一次只删除一个  不存在报错
s.remove(100)
print(s)

# 一次只删除一个  不存在不报错
s.discard(500)
print(s)

# 随机删除一个数据,不能添加参数
s.pop()
print(s)

# 清空集合
s.clear()
print(s)
