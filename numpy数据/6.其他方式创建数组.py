import numpy as np

def zerostest():
    a=np.zeros(5)
    print(a)
    #指定类型
    b=np.zeros((5,),dtype=int)
    print(b)
    #二维
    c=np.zeros((3,4))
    print(c)


def onestest():
    a=np.ones(10)
    print(a)

    b=np.ones((2,5),dtype=int)
    print(b)

#内存中
def emptytest():
    a=np.empty(8)
    print(a)

    b=np.empty((3,4))
    print(b)

#等差数列
def linespacetest():
    a=np.linspace(1,10,10)
    print(a)

    b=np.linspace(5,20,5,endpoint=True)#结尾
    print(b)

#等比数列
def logspacetest():
    a=np.logspace(0,9,10,base=2)
    print(a)

logspacetest()
