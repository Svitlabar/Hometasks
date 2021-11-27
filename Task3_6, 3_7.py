def int_func(*args):
    phrase = args[0]
    cyrillic = set("ёйцукенгшщзхъэждлорпавыфячсмитьбюієї")

    if phrase.islower():
        for i in phrase:
            if i in cyrillic:
                print("Ошибка: в тексте присутствуют символы кириллицы")
                break
            else:
                print(phrase.title())
                break
    else:
        for i in phrase.lower():
            if i in cyrillic:
                print("Ошибка: в тексте присутствуют символы кириллицы")
                break
            else:
                print("Ошибка: неправильный регистр введенного текста")
                break
    return phrase


int_func(input("Введите слово или строку с пробелом между словами на латиннице в нижнем регистре: \n"))
