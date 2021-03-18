import numpy as np

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[11,12,13],[14,15,16]])
print(a)
print(b)

#使用hstack水平拼接
r=np.hstack([a,b])
print(r)
#vstack垂直拼接
r=np.vstack([a,b])
print(r)

#concatenate的使用(默认垂直）
r1=np.concatenate((a,b),axis=0)
r2=np.concatenate((a,b))
print(r1)
print(r2)

#水平
r1=np.concatenate((a,b),axis=1)
print(r1)

# （axis=0 1 2)三维数组三个轴
a=np.arange(1,13).reshape(1,2,6)
b=np.arange(101,113).reshape(1,2,6)
print(a)
print(b)
c=np.concatenate((a,b),axis=2)
print(c)