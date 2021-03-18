import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt

#创建x,y
x=[1980,1985,1990,1995]
x_label=['1980年','1985年','1990年','1995年']
y=[1000,3000,4000,5000]
#调用bar函数
plt.bar(x,y,width=3) #width 修改柱宽度
plt.rcParams["font.sans-serif"]=['SimHei']
plt.xticks(x,x_label)
plt.ylabel("销量")
plt.xlabel("年份")
plt.title("根据年份销量对比图")
plt.show()
