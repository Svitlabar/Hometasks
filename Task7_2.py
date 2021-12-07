from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def cloth_square(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def cloth_square(self):
        cloth_square = self.v / 6.5 + 0.5
        return f"{cloth_square:.2f}"


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def cloth_square(self):
        cloth_square = 2 * self.h + 0.3
        return f"{cloth_square:.2f}"


coat_1 = Coat(32)
print("Расход ткани на пальто:", coat_1.cloth_square)

suit_1 = Suit(1.8)
print("Расход ткани на костюм:", suit_1.cloth_square)

print("Общий расход ткани:", float(coat_1.cloth_square) + float(suit_1.cloth_square))
