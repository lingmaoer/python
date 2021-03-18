import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt

x=range(-100,100)
y=[i**2 for i in x]
#绘制曲线
plt.plot(x,y)
#保存图片
# plt.savefig("result")#默认png
plt.savefig("result.jpg")
plt.show()
