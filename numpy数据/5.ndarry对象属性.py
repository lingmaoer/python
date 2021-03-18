import numpy as np

#创建一维数组
a=np.array([1,2,3,4])

#创建二维数组
b=np.random.randint(4,10,size=(2,3))
print(b)

#创建三维数组
c=np.random.randn(2,3,4)

#ndim属性
print("ndim:",a.ndim,b.ndim,c.ndim)
#shape属性
print("shape:",a.shape,b.shape,c.shape)
#dtype属性
print("dtype:",a.dtype,b.dtype,c.dtype)
#size元素总个数
print("size:",a.size,b.size,c.size)
#itemsize 每个元素所占的字节
print("iteansize:",a.itemsize,b.itemsize,c.itemsize)