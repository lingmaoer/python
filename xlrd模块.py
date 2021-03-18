import xlrd

#打开文件读取数据
data=xlrd.open_workbook("")

#获取内容
table=data.sheets()[0]
# print(table.ncols)#列数
# print(table.nrows)#行数

for i in range(table.nrows):
    print(table.row_values(i))

import pygal
#设置图
radar_char =pygal.Radar()
#定点
radar_char.x_labels = title[1:]

radar_char.add("name","data")