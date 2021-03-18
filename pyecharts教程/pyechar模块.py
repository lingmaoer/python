from pyecharts.charts import Bar
# 配置图表
from pyecharts import options as opts

c=Bar(
    Bar()
    .add_xaxis(['1','2','3','4','5','6'])
    .add_yaxis("好",[12,34,34,67,56,89])
    .add_yaxis("坏",[13,37,109,56,47,79])
    .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
                     title_opts=opts.TitleOpts(title='666'))
    .render('123.html')
)