import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(1000)
#修改住的宽度
plt.hist(x,bins=100)#10个柱装在一起

plt.show()