def my_func(a_1, a_2, a_3):
    min_arg = min(a_1, a_2, a_3)
    sum_2max = sum([a_1, a_2, a_3]) - min_arg
    print("Сумма двух наибольших аргументов = ", sum_2max)
    return sum_2max


my_func(int(input("Введите значение 1-го аргумента (целое число): ")),
        int(input("Введите значение 2-го аргумента (целое число): ")),
        int(input("Введите значение 3-го аргумента (целое число): ")))
