import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,100)
sin_y=np.sin(x)
# plt.plot(x,sin_y)

#散点图
plt.scatter(x,sin_y)
# plt.plot(x,sin_y,'o')
plt.show()

"""
从上面的示例可以看到，使用plot绘制和使用scatter绘制出来的图形是没有区别的，
但是使用p1ot绘制图形的速度由于scatter,所以如果画一堆点，而且点的形式没有差别，那么我们
使用plot,如果点的形式有差别(指点的大小和颜色不同)则必须使用scatter
"""