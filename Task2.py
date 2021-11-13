print("Пересчет времени из секунд в формат чч:мм:сс")
time_sec = int(input("Введите время в секундах: "))

hours = time_sec // 3600
minutes = int(time_sec % 3600 / 60)
sec = int(time_sec % 60)

print(f"Результат: {hours:02d}:{minutes:02d}:{sec:02d}")
