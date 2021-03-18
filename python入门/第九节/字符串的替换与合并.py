s = 'hello,python'
s1 = 'hello,python,python,python,python'
# 替换
print(s.replace('python', 'java'))
print(s1.replace('python', 'java', 2))

lst = ['hello', 'python', 'java']
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'python', 'java')
print('|'.join(t))
print(''.join(t))

print('*'.join('python'))
