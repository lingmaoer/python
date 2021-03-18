
class CarFactory:
    def creater_car(self,brand):
        if brand=='奔驰':
            return Benz()
        elif brand=="宝马":
            return BMW()
        elif brand=='比亚迪':
            return BYD()
        else:
            return '未知品牌'

class Benz:
    pass

class BMW:
    pass

class BYD:
    pass

factory = CarFactory()
c1= factory.creater_car("奔驰")
c2= factory.creater_car("宝马")