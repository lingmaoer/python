name = '张三'
age = 20
print(type(name), type(age))
print('我叫' + name + '今年' + str(age) + '岁')

print("----------------str()将其他类型转成str类型——————————————————")
a = 10
b = 198.8
c = False
print(type(a), type(b), type(c))
print("----------------int()将其他类型转成int类型——————————————————")
s1 = '128'
f1 = 98.7
s2 = '76.78'
ff = True
s3 = "hello"
print(type(s1), type(f1), type(s2), type(ff), type(s3))
print(int(s1), type(int(s1)))
print(int(f1), type(int(f1)))
#print(int(s2), type(int(s2)))#字符串为小数串
print(int(ff), type(int(ff)))
#print(int(s3), type(int(s3)))#字符串为整数串

print("----------------float()将其他类型转成float类型——————————————————")
s1 = '128'
f1 = 98.7
s2 = '76.78'
ff = True
s3 = "hello"

print(type(s1), type(f1), type(s2), type(ff), type(s3))
print(float(s1), type(float(s1)))
print(float(f1), type(float(f1)))
print(float(s2), type(float(s2)))
print(float(ff), type(float(ff)))
#print(float(s3), type(float(s3)))











