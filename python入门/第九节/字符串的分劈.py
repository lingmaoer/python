# 左侧劈分
s = 'hello world python'
lst = s.split()
print(lst)

s1 = 'hello,world,python'
lst1 = s1.split(',')
print(lst1)
lst1 = s1.split(sep=',', maxsplit=1)
print(lst1)

# 右侧劈分
print(s.rsplit())
print(s1.rsplit(sep=','))
print(s1.rsplit(sep=',', maxsplit=1))
