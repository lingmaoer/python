class Student:  # Student为类的名称（类名）由一个或多个单词组成，
    # 每个单词的首字母大写，其余小写
    # 类属性
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


# 类属性的使用
print(Student.native_pace)
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace = '天津'
print(stu1.native_pace)
print(stu2.native_pace)
print('----------类方法的使用-------------')
Student.cm()
print('----------静态方法的使用-------------')
Student.sm()