def func(a, b):
    c = a + b
    print(c)


# print(c)
# print(a)

name = '杨老师'
print(name)


def fun2():
    print(name)


fun2()


def fun3():
    global age
    age = 30
    print(age)


fun3()
print(age)
