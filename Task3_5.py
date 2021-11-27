def my_func(*args):
    sum_total = 0
    while True:
        list1 = args[0].split(" ")
        if list1[-1] == 'q':
            list1.pop()
            for i in range(len(list1)):
                try:
                    list1[i] = int(list1[i])
                except ValueError:
                    list1[i] = 0

            sum_1 = sum(list1)
            sum_total = sum_total + sum_1
            print(sum_1, "(", sum_total, ")")
            return sum_1

        else:
            for i in range(len(list1)):
                try:
                    list1[i] = int(list1[i])
                except ValueError:
                    print("Err, ошибка при введении числа")
                    list1[i] = 0

            sum_2 = sum(list1)
            sum_total = sum_total + sum_2
            print(sum_2, "(", sum_total, ")")
            args = ([input("Введите числа, разделенные пробелами, для получения их суммы (для выхода в конце строки "
                           "введите q): \n")])
            continue


my_func(input("Введите числа, разделенные пробелами, для получения их суммы, для выхода в конце строки введите q: \n"))
