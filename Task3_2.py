print("Вариант решения задачи № 1:")


def my_func(name, surname, birth_year, living_place, email, tel):
    full_name = name + " " + surname
    print("\nВаши данные: ", full_name, ",", birth_year, "года рождения", ",", "г.", living_place, ", e-mail:", email,
          ", тел.:", tel)
    return name, surname, birth_year, living_place, email, tel


my_func(name=input("Ведите Ваше имя: "), surname=input("Ведите Вашу фамилию: "),
        birth_year=input("Ведите Ваш год рождения: "), living_place=input("Ведите город Вашего проживания: "),
        email=input("Ведите Ваш e-mail адрес: "), tel=input("Ведите Ваш номер телефона: "))

print("\nВариант решения задачи 2:")


def my_func1(**kwargs):
    return kwargs


print("Ваши данные: ",
      my_func1(name=input("Ведите Ваше имя (name): "), surname=input("Ведите Вашу фамилию (surname): "),
               birth_year=input("Ведите Ваш год рождения (birth year): "),
               living_place=input("Ведите город Вашего проживания (living place): "),
               email=input("Ведите Ваш e-mail адрес (email): "), tel=input("Ведите Ваш номер телефона (tel): ")))
