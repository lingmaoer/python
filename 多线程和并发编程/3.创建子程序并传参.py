from multiprocessing import Process
from time import sleep

#定义多任务的函数
def run_test(name,age,**kwargs):
    print("子程序正在运行  name age 的值:%s %d "%(name, age))
    print("字典kwargs：",kwargs)


if __name__ == '__main__':
    print("主程序执行")
    #创建子程序
    p=Process(target=run_test,args=('xiaoming',18),kwargs={"key":12})
    #调用子进程
    p.start()