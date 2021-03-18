import numpy as np

a=np.arange(1,13).reshape((3,4))
print(a)
sub_a=a[:2,:2]
print(sub_a)

sub_a[0][0]=100
print(sub_a)
print(a)
#通过切片可以改变原来数组的值

#可以使用numpy中的copy实现
sub_aa=np.copy(a[:2,:2])
sub_aa[0][0]=200
print(a)
print(sub_aa)