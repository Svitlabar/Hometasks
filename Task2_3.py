print("1. Решение через dict")

month_no = int(input("Введите порядковый номер месяца от 1 до 12: "))

seasons_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето",
                8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}

print("Месяц", month_no, "относится к сезону", '"', seasons_dict.get(month_no), '" \n')

print("2. Решение через list:")

month_no = int(input("Введите порядковый номер месяца от 1 до 12: "))
month_list = month_no - 1

months_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]

print("Месяц", month_no, "относится к сезону", '"', months_list[month_list], '"')
