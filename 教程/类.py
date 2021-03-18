"""
class Cat:

    def eat(self):

        print("小猫爱吃鱼")

    def drink(self):

        print("小猫爱喝水")

#创建对象
tom = Cat()
#增加属性   .属性名   赋值
tom.name = 'Tom'
tom.drink()
tom.eat()
print(tom)

#addr = id(tom)
#print("%d"%addr)

#再创建一个猫对象
lazy_cat = Cat()
#lazy_cat.name = '大懒猫'
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

lazy_cat2=lazy_cat
print(lazy_cat2)
"""

'''
class Cat:

    def eat(self):
        #哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱吃鱼"% self.name)

    def drink(self):

        print("小猫爱喝水")

tom = Cat()
tom.name = 'Tom'
tom.drink()
tom.eat()
print(tom)
'''

'''
class Cat:

    def __init__(self):

        print("这是一个初始化方法")

        #self.属性名 = 属性的初始值
        self.name = 'Tom'

    def eat(self):

        print("%s 爱吃鱼"%self.name)

#使用类名()创建对象的时候，会自动调用初始化方法  __init__
tom = Cat()
tom.eat()
print(tom.name)
'''

'''
class Cat:

    def __init__(self,new_name):

        print("这是一个初始化方法")

        #self.属性名 = 属性的初始值
        self.name = new_name

    def eat(self):

        print("%s 爱吃鱼"%self.name)

#使用类名()创建对象的时候，会自动调用初始化方法  __init__
tom = Cat('Tom')
tom.eat()
print(tom.name)

lazy_cat = Cat('大懒猫')
lazy_cat.eat()
'''

'''
class Cat:

    def __init__(self,new_name):

        self.name = new_name

        print("%s 来了"%self.name)

    def __del__(self):

        print("%s 去了"%self.name)

#tom 是一个全局变量
tom = Cat('Tom')
print(tom.name)

#del 关键字可以删除吃一个对象
del tom

print("-"*60)
'''

'''
class Cat:

    def __init__(self,new_name):

        self.name = new_name

        print("%s 来了"%self.name)

    def __del__(self):

        print("%s 去了"%self.name)

    def __str__(self):

        #必须返回一个字符串
        return '我是小猫【%s】' % self.name

#tom 是一个全局变量
tom = Cat('Tom')
print(tom)

'''

# 案例1
'''
class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name} 体重 {self.weight:.2f} 公斤'

    def run(self):
        print(f"{self.name} 爱跑步，跑步锻炼身体")
        self.weight -= 0.5

    def eat(self):
        print (f"{self.name} 是吃货，吃完再减肥")
        self.weight += 1

xiaoming = Person("小明",75)

xiaoming.run()
xiaoming.eat()
print(xiaoming)
'''

# 案例2
'''
class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name} 体重 {self.weight:.2f} 公斤'

    def run(self):
        print(f"{self.name} 爱跑步，跑步锻炼身体")
        self.weight -= 0.5

    def eat(self):
        print (f"{self.name} 是吃货，吃完再减肥")
        self.weight += 1

xiaoming = Person("小明", 75)

xiaoming.run()
xiaoming.eat()
print(xiaoming)

xiaomei = Person("小美", 45)
xiaomei.eat()
xiaomei.run()
print(xiaomei)
print(xiaoming)
'''

# 案例3
'''
class HouseItem:

    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"{self.name} 占地 {self.area:.2f} 平方米"

class House:

    def __init__(self,house_type,area):

        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []
    def __str__(self):

        return (f"户型：{self.house_type}\n"
                f"总面积：{self.area:.2f}\n"
                f"剩余：{self.free_area:.2f}\n"
                f"家具：{self.item_list}")

    def add_item(self, item):

        print(f"要添加{item}")
        # 1.判断家具面积
        if item.area>self.free_area:
            print(f"{item.name}面积太大了，无法添加")
            return
        # 2.将家具的名称添加到房子
        self.item_list.append(item.name)
        self.free_area -= item.area


# 创建家具
bed = HouseItem("席梦思",60)
chest = HouseItem("衣柜", 30)
table = HouseItem("餐桌", 15)

print(bed)
print(chest)
print(table)

my_home = House("别墅",100)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)
'''

# 案例4
'''
class Gun:

    def __init__(self, model, bullet_count):
        self.model = model
        self.bullet_count = bullet_count

    def add_bullt(self, count):

        self.bullet_count += count

    def shoot(self):

        #判断子弹数量
        if self.bullet_count<=0:
            print(f"{self.model} 没有子弹了")
            return
        self.bullet_count -= 1
        print(f"{self.model} 突突突。。。{self.bullet_count}")

class Soldier:

    def __init__(self,name):
        self.name = name
        self.gun = None

    def fire(self):

        if self.gun==None:
            print(f"{self.name} 还没有枪")
            return
        print("冲啊。。。。。。。。")
        self.gun.add_bullt(20)
        self.gun.shoot()

awm = Gun("AWM",0)

#awm.bullet_count(20)
#awm.shoot()
xusanduo = Soldier("许三多")

xusanduo.gun = awm
xusanduo.fire()
'''

'''
class Woman:

    def __init__(self, name):

        self.name = name
        # 私有属性
        self.__age = 18

    # 私有方法
    def __secret(self):
        # 在对象方法内部，是可以直接访问对象的私有属性
        print(f'{self.name} 的年龄是 {self.__age}')

xh = Woman('小红')

# 私有属性,在外界不能直接访问
# print(xh.__age)
# 私有方法,在外界同样不能直接访问
# xh.__secret()

#访问私有
print(xh._Woman__age)

xh._Woman__secret ()
'''

'''
class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")

class Dog(Animal):

    # def eat(self):
    #     print("吃")
    # def drink(self):
    #     print("喝")
    # def run(self):
    #     print("跑")
    # def sleep(self):
    #     print("睡")
    def bark(self):
        print("叫")
class XiaoTiaoQuan(Dog):

    def fly(self):
        print("飞")
# wangcai = Dog()
#
# wangcai.eat()
# wangcai.run()
# wangcai.drink()
# wangcai.sleep()
# wangcai.bark()
xiaotianquan = XiaoTiaoQuan()

xiaotianquan.sleep()
xiaotianquan.eat()
xiaotianquan.drink()
xiaotianquan.bark()
xiaotianquan.run()
xiaotianquan.fly()
#如果子类，重写父类的方法，
#使用子类对象调用方法时，会调用子类的方法
'''

'''
class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")

class Dog(Animal):

    def bark(self):
        print("叫")
class XiaoTiaoQuan(Dog):

    def fly(self):
        print("飞")

    def bark(self):

        print("嘤嘤嘤")

        #super()  调用原本父类的方法
        super().bark()

        #父类名.方法(self)
        #Dog.bark(self)

xtq = XiaoTiaoQuan ()

xtq.bark()
'''

'''
class A:

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print(f"私有方法 {self.num1} {self.__num2}")

    def test(self):
        print(f"父类的公有方法{self.__num2}")
        self.__test()

class B(A):

    def demo(self):

        # 访问父类的私有属性(不能访问)
        # print(f"访问父类的私有属性{self.__num2}")
        # 访问父类的私有方法(不能)
        # print(f"访问父类的私有属性{self.__test()}")
        # 访问父类的公有属性（能）
        print(f"访问父类的公有属性{self.num1}")
        # 访问父类的公有方法
        self.test()
        pass


# 创建一个子类对象
b = B()
print(b)
b.demo()
'''

'''
class A:
    def test(self):
        print("test 方法")

class B:
    def demo(self):
        print("demo 方法")

class C(A, B):
    pass

c=C()
c.test()
c.demo()
'''

'''
class A:
    def test(self):
        print("A --- test 方法")
    def demo(self):
        print("A --- demo 方法")
class B:
    def test(self):
        print("B --- test 方法")
    def demo(self):
        print("B --- demo 方法")

class C(A, B):
    pass

c=C()
c.test()
c.demo()
#查看顺序
print(C.__mro__)
'''

'''
class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print(f"{self.name} 蹦蹦跳跳的玩===")

class XiaoTianDog(Dog):
    def game(self):
        print(f"{self.name} 飞到天上玩耍")

class Person(object):
    def __init__(self,name):
        self.name = name

    def game_with_dog(self,dog):
        print(f"{self.name}和{dog.name}快乐的玩耍")

        dog.game()

#wc = Dog("旺财")
wc = XiaoTianDog("飞天旺财")
xm = Person("小明")

xm.game_with_dog(wc)
'''

'''
class Tool(object):

    count = 0

    def __init__(self,name):
        self.name = name
        Tool.count+=1

tool1 = Tool("斧头")
tool2 = Tool("水桶")
tool3 = Tool("石头")
tool3.count=99
# print(Tool.count)
# 向上查找
print("工具对象总数%d"% tool3.count)
print(f"%d"%Tool.count)
'''

'''
class Tool(object):

    count = 0
    #类方法
    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量 %d"% cls.count)

    def __init__(self,name):
        self.name = name
        Tool.count+=1

tool1 = Tool("斧头")
tool2 = Tool("水桶")
tool3 = Tool("石头")
Tool.show_tool_count()
'''

# 静态方法   不访问实例属性/方法   也不访问类1属性/方法
'''
class Dog (object):

    @staticmethod
    def eat():
        print("吃")
# 通过类名.调用静态方法   不需要创建对象
Dog.eat()
'''

'''
class Game(object):

    top_score = 0

    def __init__(self,play_name):
        self.play_name = play_name

    @staticmethod
    def show_help():
        print("帮助信息：=====")

    @classmethod
    def show_top_score(cls):
        print(f"历史记录 {cls.top_score}")

    def start_game(self):
        print(f"{self.play_name}  开始游戏")

#游戏帮助信息
Game.show_help()
#历史最高分
Game.show_top_score()
# 游戏对象
game = Game("小明")
#开始游戏
game.start_game()
'''

'''
class MusicPlayer (object):

    def __init__(self):
        print ("播放器初始化")

    def __new__(cls, *args, **kwargs):
        # 创建方法时，new方法会被自动调用
        print ("创建对象，分配空间")
        # 为对象分配空间
        instance = super ().__new__ (cls)
        # 返回对象的引用
        return instance


player = MusicPlayer()

print (player)
'''

'''
class MusicPlayer (object):
    # 记录第一个被创建对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):
        # 判断类属性是否空对象
        if cls.instance is None:
            # 调用父类方法，分配空间
            cls.instance = super ().__new__ (cls)
        # 返回类属性保存的对象引用
        return cls.instance


player1 = MusicPlayer ()
print (player1)
player2 = MusicPlayer ()
print (player2)
'''

'''
class MusicPlayer (object):
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 判断类属性是否空对象
        if cls.instance is None:
            # 调用父类方法，分配空间
            cls.instance = super ().__new__ (cls)
        # 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        # 判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return
        # 如果没有执行过，执行初始化
        print ("初始化方法")
        # 修改类属性的标记
        MusicPlayer.init_flag = True


player1 = MusicPlayer ()
print (player1)
player2 = MusicPlayer ()
print (player2)
'''
