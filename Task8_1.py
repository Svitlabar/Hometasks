class Data:

    def __init__(self, dd_mm_yyyy):
        self.d = dd_mm_yyyy

    @classmethod
    def int_number(cls, obj):
        try:
            dd, mm, yyyy = map(int, obj.split("-"))
        except ValueError:
            print("\nВведите дату в правильном формате в виде чисел")
        else:
            print("\nВведенные данные преобразованы в числа", dd, mm, yyyy)
        return cls(obj)

    @staticmethod
    def date_valid(obj_1):
        try:
            dd, mm, yyyy = map(int, obj_1.split("-"))
        except ValueError:
            pass
        else:
            if 1999 < yyyy < 2022 and 1 <= mm <= 12 and 1 <= dd <= 31:
                if mm == 2 and yyyy % 4 == 0 and dd > 29:
                    print("Введена неправильная дата")
                elif mm == 2 and yyyy % 4 != 0 and dd > 28:
                    print("Введена неправильная дата")
                elif mm in (1, 3, 5, 7, 9, 10, 12) and dd >= 31:
                    print("Введена неправильная дата")
                elif mm in (4, 6, 8, 11) and dd >= 30:
                    print("Введена неправильная дата")
                else:
                    print("Дата введена корректно")
            else:
                print("Введена несуществующая дата или дата вне указанного диапазона")


date = input('Требуемый диапазон дат: 01.01.2000-31.12.2021\nВведите дату в формате "день-месяц-год": ')

date_1 = Data.int_number(date)
Data.date_valid(date)
