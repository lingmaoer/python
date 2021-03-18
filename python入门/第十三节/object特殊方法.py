a = 20
b = 100
c = a + b
d = a.__add__(b)

print(c)
print(d)


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student("张三")
stu2 = Student('李四')
stu3 = stu1.__add__(stu2)
print(stu3)

stu3 = stu1 + stu2
print(stu3)

print('-'*50)
lst=[11,22,33,44]
print(len(lst))
print(lst.__len__())
print(len(stu1))