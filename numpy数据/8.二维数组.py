import numpy as np

a=np.arange(1,13)
print(a)
#修改数组形状
a=a.reshape((4,3))
print(a)
print(a[2])
print(a[1][2])

#切片
print(a[:,:])
print(a[:,1])
print(a[:,0:2])
print(a[::2,:])
print(a[::2,0:2])

print(a[1][2])
print(a[1,2])
print(a[1,2],a[2][0])
print(np.array([a[1,2],a[2][0]]))

print(a[(2,3),(1,2)])

print(a[-1])
print(a[::-1])
print(a[::-1,::-1])