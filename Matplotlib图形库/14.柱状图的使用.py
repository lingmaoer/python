import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np

real_name=["千与千寻","玩具总动员4","黑衣人：全球追击"]
#票房
real_num1=[7548,4013,1673]
real_num2=[5453,1840,1080]
real_num3=[4348,2345,1890]

x=np.arange(len(real_name))
plt.bar(x,real_num1,alpha=0.5,width=0.3,label=real_name[0])
plt.bar([i+0.3 for i in x],real_num2,alpha=0.5,width=0.3,label=real_name[1])
plt.bar([i+0.6 for i in x],real_num3,alpha=0.5,width=0.3,label=real_name[2])
x_label=["第一天","第二天","第三天"]
plt.xticks([i+0.3 for i in x],x_label)
plt.ylabel("票房数")
plt.rcParams['font.sans-serif']=['SimHei']
plt.legend()
plt.title("三天三部电影票房数")
plt.show()