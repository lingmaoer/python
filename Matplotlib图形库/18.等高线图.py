import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
#计算x,y相交点
X,Y=np.meshgrid(x,y)
#计算z
Z=np.sqrt(X**2+Y**2)
#绘制等高线图
# plt.contour(X,Y,Z)
plt.contourf(X,Y,Z)

plt.show()