def fun(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


fun(10, 20, 30)  # 函数调用时的参数传递，称为位置传参
lst = [11, 22, 33]  # 在函数调用时，将列表中的每个元素都转换为位置实参传入
fun(*lst)
fun(a=100, b=200, c=300)  # 函数的调用，所以是关键字实参
dic = {'a': 100, 'b': 200, 'c': 300}
fun(**dic)


def fun1(a, b=100):  # b是在函数的定义处，所以b是形参，而且进行了赋值，所以b称为默认值形参
    print('a=', a)
    print('b=', b)


def fun2(*args):  # 个数可变的位置形参
    pass


def fun3(**kwargs):  # 个数可变的关键字形参
    pass


def fun4(a, b, *, c, d):  # 从*之后的参数，在函数调用时，只能采用关键字参数传递
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


# fun4(10, 20, 30, 40)  # 位置实参传递
fun4(a=10, b=20, c=30, d=40)  # 关键字实参传递
fun4(10, 20, c=30, d=40)  # 前两个参数，采用的是位置实参传递，而c, d采用的是关键字实参传递


# 函数定义时的形参的顺序问题
def fun5(a, b, *, c, d, **args):
    pass


def fun6(*args, **args2):
    pass


def fun7(a, b=10, *args, **args2):
    pass
