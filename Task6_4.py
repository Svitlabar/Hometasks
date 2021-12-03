import random


class Car:

    def __init__(self, s, c, n, bul):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = bul
        self.show_speed()

    def go(self):
        print("поехала\n")

    def stop(self):
        print("остановилась\n")

    def turn(self):
        i = random.randint(1, 2)
        if i == 1:
            print("повернула вправо\n")
        else:
            print("повернула влево\n")

    def show_speed(self):
        print(self.name, "скорость", self.speed, "км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(self.name, "скорость", self.speed, "км/ч - превышение скорости")
        else:
            print(self.name, "скорость", self.speed, "км/ч")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(self.name, "скорость", self.speed, "км/ч - превышение скорости")
        else:
            print(self.name, "скорость", self.speed, "км/ч")


class PoliceCar(Car):
    pass


auto_1 = TownCar(80, "red", "Porsche", False)
auto_1.go()

auto_2 = TownCar(40, "white", "VW", False)
auto_2.turn()

auto_3 = WorkCar(60, "brown", "Камаз", False)
auto_3.go()

auto_4 = WorkCar(0, "black", "Skoda", False)
auto_4.stop()

auto_5 = SportCar(130, "blue", "Ferrari", False)
auto_5.go()

auto_6 = PoliceCar(30, "white/black", "Suzuki", True)
auto_6.turn()

auto_7 = PoliceCar(0, "white/black", "Mazda", True)
auto_7.stop()
