# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#
#     def start(self):
#         print('汽车已启动')
#
#
# car = Car('宝马X5')
# car.start()
# print(car.brand)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
stu.show()

print(stu.name)
# print(stu.__age)
print(dir(stu))
print(stu._Student__age)  # 在类的外部可以通过_Student__age进行访问
