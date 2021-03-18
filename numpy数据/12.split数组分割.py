import numpy as np

#传递整数，平均分割
a=np.arange(1,9)
r=np.split(a,4)
print(r)

#传递数组，按位置分割
r=np.split(a,[4,6])
print(r)

#二维数组进行分割
a=np.arange(1,17).reshape(4,4)
print(a)
print("axis=0 垂直方向 平均分割")
r,w,k=np.split(a,[2,3],axis=0)
print(r,w,k)

print("axis=1 水平方向 平均分割")
r,w=np.split(a,2,axis=1)
print(r,w)

#hsplit水平分割
r,w=np.hsplit(a,2)
print(r)
print (w)
r,w=np.hsplit(a,[3])
print(r)
print (w)

#vsplit垂直分割
r,w=np.vsplit(a,2)
print(r)
print (w)
r,w=np.vsplit(a,[1])
print(r)
print (w)