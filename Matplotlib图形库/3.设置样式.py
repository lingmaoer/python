import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,4,9,16,25]
#宽度
plt.plot(x,y,linewidth=5)
#添加x,y名称
plt.xlabel("x")
plt.ylabel("y=x^2")
#标题
plt.rcParams["font.sans-serif"]=['SimHei']
plt.title("折线图")
plt.show()