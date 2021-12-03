class Stationery:

    def __init__(self, t):
        self.title = t
        self.draw()

    def draw(self):
        print("Запуск зарисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск зарисовки карандашом")


class Pencil(Stationery):
    def draw(self):
        print("Запуск зарисовки ручкой")


class Handle(Stationery):
    def draw(self):
        print("Запуск зарисовки маркером")


task_1 = Pen("Доска")

task_2 = Pencil("Картина")

task_3 = Handle("Натюрморт")
