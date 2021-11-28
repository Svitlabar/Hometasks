n = input("Введите значение n (целое число): ")
try:
    n = int(n)
except ValueError:
    print("Ошибка, необходимо вводить целое число")
else:

    def fact():
        fact_1 = 1
        for m in range(1, n + 1):
            fact_1 = fact_1 * m
            yield fact_1


    print(fact())

    for el in fact():
        print(el)
