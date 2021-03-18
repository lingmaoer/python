class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    def info(self):
        print(self.name, self.age, self.stu_no)


class Teacher(Person):
    def __init__(self, name, age, teachyear):
        super().__init__(name, age)
        self.teachyear = teachyear

    def info(self):
        print(self.name, self.age, self.teachyear)


tea = Teacher('李四', 34, 10)
stu = Student('张三', 20, '1001')


tea.info()
stu.info()
