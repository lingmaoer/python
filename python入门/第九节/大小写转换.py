s = 'hello,python'
a = s.upper()
print(s, id(s))
print(a, id(a))

b = s.lower()  # 转换之后会产生一个新对象
print(b, id(b))
print(s, id(s))

print(b == s)  # 值相等
print(b is s)  # 地址不同

s2 = 'hello,Python'
print(s2.swapcase())  # 大写变小写
print(s2.capitalize())  # 第一个字母变大写，其他都变小写

print(s2.title())  # 每个单词首字母大写
