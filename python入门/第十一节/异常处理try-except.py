try:
    n1=int(input("输入一个整数："))
    n2=int(input("输入一个整数："))
    result=n1/n2
    print("结果为：",result)
except ZeroDivisionError:
    print("除数不能为 0 ")
except ValueError:
    print("只能输入数字")
except BaseException as e:
    print(e)
print("程序结束")