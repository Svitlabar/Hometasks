def my_fun(p_1, p_2):
    try:
        p_1 = int(p_1)
        p_2 = int(p_2)

        div = p_1 / p_2
    except ZeroDivisionError:
        print("Деление на 0")
    except ValueError:
        print("Неправльное исходное значение. Делитель и/или делимое введены не как целое число")
    else:
        print(div)
        return div


my_fun(input("Введите делимое (целое число): "), input("Введите делитель (целое число): "))
