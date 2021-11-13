print("Задача: найти самую большую цифру в числе.")
n = int(input("Введите целое положительное число: "))

max_digit = int(0)
x = n % 10

while n > 0:
    if x > max_digit:
        max_digit = x
        x = n % 10
        n = n // 10
    else:
        x = n % 10
        n = n // 10

print("Самая большая цифра в числе: ", max_digit)
