t = ('python', 'world', 98)
print(t)
print(type(t))

t2 = 'python', 'world', 98
print(t2)
print(type(t2))

# 只有一个数据，','不能省
t3 = ('python',)
print(t3)
print(type(t3))

t4 = ()
t5 = tuple()
print(t4, t5)

t = tuple(('python', 'world', 98))
