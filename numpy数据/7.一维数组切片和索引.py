import numpy as np

a=np.arange(10)
print(a)
#索引访问
print(a[0])
print(a[5])
print(a[-1])
#切片操作
print(a[:])
print(a[3:])
print(a[3:5])
print(a[1::2])
#切片负索引
print(a[::-1])
print(a[-5:-2])