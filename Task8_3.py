class MyOwnErr(Exception):

    def __init__(self, num):
        self.num = num


my_list = []
while True:
    my_list_item = input("Введите элемент списка (чтобы остановить ввод данных введите stop): ")
    if my_list_item == "stop":
        break
    elif my_list_item == '':
        print("Введена пустая строка")
        continue
    else:
        try:
            for i in my_list_item:
                if i not in "0123456789":
                    raise MyOwnErr("Введенный текст не является целым положительным числом")
        except (MyOwnErr) as err:
            print(err)
        else:
            my_list = my_list + [int(my_list_item)]
            print(my_list)

