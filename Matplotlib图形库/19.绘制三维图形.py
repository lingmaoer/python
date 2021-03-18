import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#创建X，Y，Z
x=[1,1,2,2]
y=[3,4,4,3]
z=[1,100,1,1]

figure=plt.figure()
#创建Axes3D对象

ax=Axes3D(figure)
ax.plot_trisurf(x,y,z)

plt.show()