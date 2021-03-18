# 比较运算符

a, b = 10, 20
print("a>b吗？", a > b)
print("a<b吗？", a < b)
print("a>=b吗？", a >= b)
print("a<=b吗？", a <= b)
print("a==b吗？", a == b)
print("a!=b吗？", a != b)

'''’一个=称为赋值运算符，==称为比较运算符
一个变量由三部分组成，标识，类型，值
==比较的是值还是标识呢?比较的是值
比较对象的标识使用 is
'''
a = 10
b = 10
print(a == b)  # value相等
print(a is b)  # id相等

list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)  # value相等
print(list1 is list2)  # id不相等
print(list1 is not list2)
