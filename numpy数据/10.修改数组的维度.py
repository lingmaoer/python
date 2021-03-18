import numpy as np

a=np.arange(1,25)
print(a)

#一维变二维
b=a.reshape(4,6)
print(b)

#一维变三维
c=a.reshape(2,3,4)
print(c)

#一维变二维
bb=np.reshape(a,(3,8))
print(bb)

#一维变三维
cc=np.reshape(a,(4,3,2))
print(cc)

# 多维变一维
# a=bb.reshape(24)
a=bb.reshape(-1)
print(a)

#ravel
a=bb.ravel()
print(a)

#flatten
a=bb.flatten()
print(a)
