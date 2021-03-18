import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np

#10种大小，100种颜色
# 创建x
np.random.seed(0)#每次随机数不变
x=np.random.rand(100)
y=np.random.rand(100)
#100种大小
size=np.random.rand(100)*1000
#100种颜色
color=np.random.rand(100)

plt.scatter(x,y,s=size,c=color,alpha=0.7)#s点的大小 c颜色 alpha=透明度

plt.show()

'''
注意：点的个数和颜色的个数要相同
      点的个数和点大小的个数可以不同，如果点的个数大于大小的个数，则会循环获取大小
'''
