print(bool(0))
print(bool(8))


def func(num):
    odd = []
    event = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            event.append(i)
    return odd,event


lst = [10, 29, 34, 23, 44, 53, 55]
print(func(lst))

#1.如果函数没有返回值
#2.函数的返回值，如果是一个，直接返回类型
#2.函数的返回值，如果是多个，返回结果元组
def fun1():
    print('hello')

fun1()

def fun2():
    return 'hello'
res=fun2()
print(res)

def fun3():
    return 'hello','world'
print(fun3())






