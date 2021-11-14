print("Исходные данные задачи: \n    a - количество километров пробежки за 1-день, км \n    "
      "b - количество километров пробежки за день N, км")

a = int(input("Введите а: "))
b = int(input("Введите b: "))

day_no = int(1)  # N
increase_km = a

if b >= a:
    while True:
        day_no += 1
        increase_km = increase_km * 1.1
        if increase_km >= b:
            break
        elif increase_km < b:
            continue

    print("Номер дня, при котором достигнут результат", b, "км, (N):", day_no)
else:
    print("Введены неправильные значения, b не может быть меньше а")
