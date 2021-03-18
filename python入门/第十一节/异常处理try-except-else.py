try:
    n1=int(input("输入一个整数："))
    n2=int(input("输入一个整数："))
    result=n1/n2

except BaseException as e:
    print("出错了",e)

else:
    print("结果为：",result)
print("程序结束")