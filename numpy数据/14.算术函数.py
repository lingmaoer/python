import numpy as np


a=np.arange(9).reshape((3,3))
b=np.array([10,10,10])
print("加法")
print(np.add(a,b))
print(a+b)
print("减法")
print(np.subtract(a,b))
print(a-b)

#out参数使用
y=np.empty((3,3),dtype=int)
print(y)
np.multiply(a,10,out=y)
print(y)

#三角函数
a=np.array([0,30,60,90])
print(np.sin(a*np.pi/180))
print(np.cos(a))
print(np.tan(a))

#四舍五入around ceil floor
a=np.array([1.0,4.55,123,0.567,25.223])
print(np.around(a))#四舍五入
print(np.ceil(a))#向上取整
print(np.floor(a))#向下取整


#聚合函数
a=np.arange(1,13).reshape((3,4))
print(a)
print(np.power(a,2))

# power()  out使用
x=np.arange(5)
y=np.zeros(10)
print (np.power (2, x, out=y[:5]))


#一维数组的中位数
a=np.array([4,3,2,5,2,1])
print(np.median(a))

#二维数组  要通过axisz指定轴
a=np.arange(1,13).reshape((3,4))
print("垂直方向",np.median(a,axis=0))
print("竖直方向",np.median(a,axis=1))

#mean  求平均值
#一维
a=np.array([4,3,2,5,2,1])
print(np.mean(a))
#二维
#二维数组  要通过axisz指定轴
a=np.arange(1,13).reshape((3,4))
print("垂直方向",np.mean(a,axis=0))
print("竖直方向",np.mean(a,axis=1))

# sum() min()  max()
a=np.array([4,3,2,5,2,1])
print(np.max(a))
print(np.min(a))
print(np.sum(a))

#argmax  argmin
print(np.argmax(a))
print(np.argmin(a))