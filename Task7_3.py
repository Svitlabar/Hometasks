class Cell:

    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        return self.cell - other.cell if (self.cell - other.cell) > 0 else print("Вычитание невозможно")

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return f" {int(self.cell / other.cell)}\n"

    def make_order(self, row):
        return f"{'*' * row}\n" * (self.cell // row) + f"{'*' * (self.cell % row)}\n"


cell_1 = Cell(20)
cell_2 = Cell(15)

print("Сумма клеток: ", cell_1 + cell_2)
print("Разность клеток: ", cell_1 - cell_2)
print("Произведение клеток: ", cell_1 * cell_2)
print("Частное клеток: ", cell_1 / cell_2)

print(cell_1.make_order(8))
print(cell_2.make_order(6))
