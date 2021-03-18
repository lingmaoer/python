import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,1000)

sin_y=np.sin(x)
plt.subplot(2,2,1)

#修改x,y坐标
plt.xlim(-5,20)
plt.ylim(-2,2)
plt.plot(x,sin_y)

plt.subplot(2,2,4)
plt.plot(x,np.cos(x))
plt.show()