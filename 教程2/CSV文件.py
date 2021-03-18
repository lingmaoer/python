import csv

with open('CSV文件.csv','r')as f:
    #读取文件
    a_csv = csv.reader(f)
    # print(list(a_csv))
    for i in a_csv:
        print(i)

with open('CSV文件.csv','w')as f:
    #写入文件
    b_csv = csv.writer(f)
    b_csv.writerow(['姓名','学号','性别'])
    b_csv.writerow(['李明', '111111', '男'])
    c = [['张三','222222','男'],['李四','333333','女']]
    b_csv.writerows(c)