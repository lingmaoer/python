import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np

x=np.random.normal(0,0.8,1000)
y=np.random.normal(-2,1,1000)
z=np.random.normal(3,2,1000)
kwargs=dict(bins=100,alpha=0.5)
plt.hist(x,**kwargs)
plt.hist(y,**kwargs)
plt.hist(z,**kwargs)
plt.show()