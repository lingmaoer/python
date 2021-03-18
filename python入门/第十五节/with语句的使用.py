with open('a.txt', 'r') as file:
    print(file.read())


# MyContentMgr实现了特殊方法__enter__(),__exit__()称为该类对象遵守了上下文管理器协议
# 该类对象的实例对象，称为上下文管理器
class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用了')

    def show(self):
        print('show方法被调用了')


with MyContentMgr() as file:
    file.show()