'''
#函数
def fun1():
    """   test1  """
    print("in the func1")
    return 0
x=fun1()
#过程
def fun2():
    """   test2  """
    print("in the func2")
y=fun2()
print("return fun1 is %s"%x)
print("return fun2 is %s"%y)
'''

'''
import time
def logger():
    time_formate= '%Y-%m-%d %X'
    time_current = time.strftime(time_formate)
    with open("日志.text",'a+') as f:
        f.write('%s end action\n'%time_current)

def test1():
    print("in the text1")
    logger ()
def test2():
    print("in the text2")
    logger ()
def test3():
    print("in the text3")
    logger ()
test1()
test2()
test3()
'''

'''
def test1():
    print("in the text1")

def test2():
    print("in the text2")
    return 0
def test3():
    print("in the text3")
    return 1,'hello',{1:2},[2,5]
x=test1()
y=test2()
z=test3()
print(x)
print(y)
print(z)
'''

'''
def test(x,y,z):
    print(x)
    print(y)
    print(z)
test(1,2,3)
test(3,2,1)
test(3,z=2,y=5)
'''

'''
#默认参数
def test(x,y=2):
    print(x)
    print(y)
test(1)
test(2,5)
'''

'''
def test(x,*args):
    print(x)
    print(args)

test(1,2,3,4,5)
test(*[1,2,3,4,5])
'''

'''
#关键字参数，转换成字典
def test(**kwargs):
    print(kwargs['name'])
    print(kwargs['sex'])
    print(kwargs['police'])

test(name='1',sex='2',police='3')
test(**{'name':'1','sex':'2','police':'3'})
'''

'''
#局部变量,数字去，字符串
a=5
def test():
    global a
    print(a)
    a=3
    print(a)
test()
print(a)
'''

'''
a=['1','2','3']
def test():
    a[0]='9'
    print(a)
test()
print(a)
'''

'''
#递归
def cale (n):
    print(n)
    if(int(n/2)>0):
        return cale(int(n/2))
cale(20)
'''


'''
def  add(a,b,f):
    return  f(a)+f(b)
num = add(2,-5,abs)
print(num)
'''

a = input("请输入算术：")
print(eval(a))




