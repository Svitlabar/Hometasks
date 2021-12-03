class Road:

    def __init__(self, l, w):
        self._length = l
        self._width = w
        self.weight()

    def weight(self):
        print(f"Масса 1 кг асфальта толщиной 1 см: 20 кг, \nтолщина полотна: 10 см, \nдлина объекта: {self._length} м,\n"
              f"ширина объекта: {self._width} м \n\nМасса объекта: {self._length * self._width * 20 * 10 / 1000} т")


road_1 = Road(200, 3)
