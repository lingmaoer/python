import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pyplot as plt
import numpy as np

#准备男、女的人数及比例
man=71351
woman=68187
man_perc=man/(woman+man)
woman_perc=woman/(woman+man)
#添加名称
labels=["男","女"]
#添加颜色
colcors=['blue','red']
#绘图   explode=分裂   autopct=显示百分比
paches,texts,autotexts=plt.pie([man_perc,woman_perc],labels=labels,colors=colcors,explode=(0,0.05),autopct='%0.1f%%')
#修改图中字体颜色
for text in autotexts:
    text.set_color("white")
#修改字体大小
for text in texts+autotexts:
    text.set_fontsize(20)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.show()