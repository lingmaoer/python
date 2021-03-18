import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x=np.arange(5)
y=np.random.randint(-5,5,5)
plt.subplot(1,2,1)
#更改颜色
plt.bar(x,y,color='blue')
#水平0位置加线条
plt.axhline(0,color='blue',linewidth=2)
plt.subplot(1,2,2)
# 竖直0位置加线条
plt.axvline(0,color='red',linewidth=2)
plt.barh(x,y,color='green')
plt.show()