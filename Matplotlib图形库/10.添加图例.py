import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(1,10,100)
#-g绿色实线  --g绿色虚线
plt.plot(x,x+0,'-g',label='-g')
plt.plot(x,x+1,'--g',label='--g')
plt.plot(x,x+2,'-.r',label='-.r')
plt.plot(x,x+3,':b',label=':b')
plt.plot(x,x+4,'.k',label='.k')
plt.plot(x,x+5,',c',label=',c')
plt.plot(x,x+6,'*y',label='*y')
plt.plot(x,x+6,'dr',label='dr')
#默认在左上角upper left  fancybox=边框 framealpha=透明度 shadow=阴影 borderpad=边框宽度
plt.legend(loc="lower right",fancybox=True,framealpha=1,shadow=True,borderpad=1)
plt.show()