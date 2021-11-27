print("Решение № 1 (через цикл):")


def my_func(x, y):
    if x <= 0 or y >= 0:
        print("Введены некорректные значения x и/или y")
    else:
        i = 1
        mult = 1
        while True:
            if i < abs(y):
                mult = mult * x
                i += 1
                continue
            if i == abs(y):
                result = 1 / (mult * x)
                print(result)
                return result


my_func(float(input("Введите положительное число х: ")), int(input("Введите целое отрицательное число y: ")))

print('\n \nРешение № 2 через "**"')


def my_func1(x, y):
    if x <= 0 or y >= 0:
        print("Введены некорректные значения x и/или y")
    else:
        result = x ** y
        print(result)
        return result


my_func1(float(input("Введите положительное число х: ")), int(input("Введите целое отрицательное число y: ")))
