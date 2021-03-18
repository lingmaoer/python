import numpy as np

a=np.arange(1,25).reshape((8,3))
print(a)
# transpose函数进行转置

b=np.transpose(a)
print(b,b.shape)

#a.T也可以
print(a.T)

#numpy中的transpose()
c=np.transpose(a)
print(c)

#多维数组转置
a=a.reshape((2,3,4))
print(a,a.shape)
print("对于三维a[i][j][k] 进行转置 默认将i和k交换")
b=np.transpose(a)
print(b,b.shape)

 #(2,3,4)-->(3,4,2)
c=np.transpose(a,(1,2,0))
print(c,c.shape)