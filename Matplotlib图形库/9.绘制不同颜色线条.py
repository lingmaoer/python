import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(1,10,100)
#-g绿色实线  --g绿色虚线
plt.plot(x,x+0,'-g')
plt.plot(x,x+1,'--g')
plt.plot(x,x+2,'-.r')
plt.plot(x,x+3,':b')
plt.plot(x,x+4,'.k')
plt.plot(x,x+5,',c')
plt.plot(x,x+6,'*y')
plt.show()