class Matrix:

    def __init__(self, m):
        self.m = m

    def __str__(self):
        return f"{str(self.m[0][0])} {' ' * (5 - len(str(self.m[0][0])))} {str(self.m[0][1])}\n" \
               f"{str(self.m[1][0])} {' ' * (5 - len(str(self.m[1][0])))} {str(self.m[1][1])}\n" \
               f"{str(self.m[2][0])} {' ' * (5 - len(str(self.m[2][0])))} {str(self.m[2][1])}\n"

    def __add__(self, other):
        if len(other.m) > 3:
            print("Неравное количество списков в списке")
        else:
            return f"{str(self.m[0][0] + other.m[0][0])} {' ' * (5 - len(str(self.m[0][0] + other.m[0][0])))} " \
                   f"{str(self.m[0][1] + other.m[0][1])}\n" \
                   f"{str(self.m[1][0] + other.m[1][0])} {' ' * (5 - len(str(self.m[1][0] + other.m[1][0])))}" \
                   f" {str(self.m[1][1] + other.m[1][1])}\n" \
                   f"{str(self.m[2][0] + other.m[2][0])} {' ' * (5 - len(str(self.m[2][0] + other.m[2][0])))}" \
                   f" {str(self.m[2][1] + other.m[2][1])}\n"


matrix_1 = Matrix([[31, 22], [8, 43], [11, 86]])
print(matrix_1)

matrix_2 = Matrix([[21, 55], [55, 57], [74, 16]])
print(matrix_1 + matrix_2)
