import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,1000)
sin_y=np.sin(x)
#绘制图形
plt.plot(x,sin_y)


cos_y=np.cos(x)
#绘制图形
plt.plot(x,cos_y)
plt.savefig("sin cos.jpg")
plt.show()