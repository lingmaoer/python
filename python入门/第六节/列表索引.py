lst = ['hello', 'world', 98, 'hello']
print(lst.index('hello'))  # 如果列表中有重复的变量，只返回第一个索引
print(lst.index('hello', 1, 3))  # 从1-2中寻找
print(lst.index('hello', 1, 4))  # 从1-3中寻找

