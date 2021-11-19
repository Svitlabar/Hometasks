print("Введите элементы для составления списка")

element1 = input("Введите 1-й элемент списка: ")
element2 = input("Введите 2-й элемент списка: ")
element3 = input("Введите 3-й элемент списка: ")
element4 = input("Введите 4-й элемент списка: ")
element5 = input("Введите 5-й элемент списка: ")
element6 = input("Введите 6-й элемент списка: ")
element7 = input("Введите 7-й элемент списка: ")

my_list = [element1, element2, element3, element4, element5, element6, element7]
print("Полученный список: ", my_list)

for i in range(1, len(my_list)):
    if i % 2 == 0:
        i = i + 1
    else:
        var1 = my_list[i]
        my_list.remove(var1)
        my_list.insert(i - 1, var1)

print("Полученный список: ", my_list)
