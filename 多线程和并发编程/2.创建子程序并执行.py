from multiprocessing import Process

def run_test():
    print("==========test====")
if __name__ == '__main__':
    print("主程序执行")
    #创建子程序，target接受执行的任务
    p=Process(target=run_test())
    #调用子进程
    p.start()