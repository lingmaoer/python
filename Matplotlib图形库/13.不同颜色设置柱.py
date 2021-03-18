import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x=np.arange(5)
y=np.random.randint(-5,5,5)
plt.subplot(1,2,1)
#更改颜色
v_bar=plt.bar(x,y,color='blue')

for bar,height in zip(v_bar,y):
    if height<0:
        bar.set(color="red")

#
plt.show()