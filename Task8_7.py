class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = f"{str(a) + str(b)}i" if b < 0 else f"{str(a)}+{str(b)}i"

    def __add__(self, other):
        return f"{self.a + other.a}{self.b + other.b}i" if self.b < 0 \
            else f"{self.a + other.a}+{self.b + other.b}i"

    def __mul__(self, other):
        return f"{self.a * self.b - other.a * other.b}{self.a * other.b - self.b * other.a}i" \
            if (self.a * other.b - self.b * other.a) < 0 \
            else f"{self.a * self.b - other.a * other.b}+{self.a * other.b - self.b * other.a}i"


number_1 = ComplexNumber(4, -2)
print("Комплексное число 1: ", number_1.z)

number_2 = ComplexNumber(-0.2, -0.5)
print("Комплексное число 2: ", number_2.z, "\n")

print("Сумма комплексных чисел:", number_1 + number_2)
print("Произведение комплексных чисел:", number_1 * number_2)
