def fun(a, b=100):
    print(a, b)


fun(100)
fun(10, 20)


def fun1(*args):  # 可变的位置参数
    print(args)


fun1(123)
fun1(123, 234, 456)


def fun2(**kwargs):  # 可变的关键字参数
    print(kwargs)


fun2(a=10)
fun2(a=10, b=30, c=10)

# 在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，
# 要求，个数可变的位置形参，放在个数可变的关键字形参之前
# print(set((1,2,3)))
