class Student:  # Student为类的名称（类名）由一个或多个单词组成，
    # 每个单词的首字母大写，其余小写
    native_pace = '河南'  # 直接写在类里的变量，称为类属性

    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def eat(self):
        print("学生在吃饭。。")

    # 静态方法
    @staticmethod
    def sm():
        print("我是静态方法")

    # 类方法
    @classmethod
    def cm(cls):
        print("我是类方法")


print(id(Student))
print(type(Student))
print(Student)
stu = Student("张三", 18)
print(id(stu))
print(type(stu))
print(stu)
stu.eat()
stu.cm()
stu.sm()
print("-" * 50)
Student.eat(stu)  # 36行与32行代码功能相同，都是调用eat方法
