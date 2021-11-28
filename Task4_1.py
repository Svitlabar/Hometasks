from sys import argv

name, hourly_rate, total_hours, bonus_percent = argv

try:
    hourly_rate = float(hourly_rate)
    total_hours = float(total_hours)
    bonus_percent = float(bonus_percent)
except ValueError:
    print("Ошибка введения значений")
else:
    if hourly_rate > 0 and total_hours > 0 and bonus_percent >= 0:
        salary = int(hourly_rate) * int(total_hours) * (100 + int(bonus_percent)) / 100
        print("Зарплата = почасовая ставка * количество отработанных часов + бонус, % = ", salary, "USD")
    else:
        print("Ошибка введения значений")
