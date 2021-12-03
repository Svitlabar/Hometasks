class Worker:

    def __init__(self, n, s, p, dict):
        self.name = n
        self.surname = s
        self.position = p
        self._income = dict
        self.get_full_name()
        self.get_total_income()


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(f"Total income: {sum(self._income.values())} EUR")


manager_1 = Position("Pierre", "Cardin", "manager", {"wage": 20000, "bonus": 2000})

manager_2 = Position("Vivienne", "Westwood", "manager", {"wage": 30000, "bonus": 3500})

manager_3 = Position("Someone", "Else", "manager", {"wage": 10000, "bonus": 1000})
