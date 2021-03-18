#不可变序列，没有增删改操作
print('----------可变序列-列表，字典----------------------')
lst=[10,20,30]
print(id(lst))
lst.append(200)
print(id(lst))

print('----------不可变序列-字符串，元组----------------------')
s='hello'
print(id(s))
s+='world'
print(id(s))
print(s)