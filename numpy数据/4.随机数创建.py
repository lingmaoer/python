import numpy as np

def randomtest():
    # 使用random函数创建一维数组(0.0,1.0)
    a=np.random.random(size=5)
    print(a)
    print(type(a))

    # 使用random函数创建二维数组(0.0,1.0)
    b=np.random.random(size=(3,4))
    print(b)
    print(type(b))

    # 使用random函数创建二维数组(0.0,1.0)
    c=np.random.random(size=(2,3,4))
    print(c)
    print(type(c))

def randinttest():
    # 随机整数
    # 0，5  一维数组
    d=np.random.randint(6,size=10)
    print(d)

    #5,10 二维数组
    e=np.random.randint(5,11,size=(4,3))
    print(e)

    #5,10 3维数组
    f=np.random.randint(5,11,size=(2,4,3))
    print(f)

    # dtype的使用
    g=np.random.randint(10,size=5)
    print(g.dtype)
    g=np.random.randint(10,size=5,dtype=np.int64)
    print(g.dtype)


#创建标准的正态分布，期望为0，方差为1
def randntest():
    a=np.random.randn(4)
    print(a)

    #二维
    a=np.random.randn(2,3)
    print(a)

    #三维
    a=np.random.randn(2,3,4)
    print(a)

# 创建指定期望和方差的正态分布
def normaltest():
    a=np.random.normal(size=5)   #默认期望loc=0.0，方差scale=1.0
    print(a)

    b=np.random.normal(loc=2,scale=3,size=(3,4))
    print(b)
