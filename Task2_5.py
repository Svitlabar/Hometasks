rating_initial = [8, 6, 3, 3, 2]

print("Текущий рейтинг: ", rating_initial)

new_element = int(input("Введите новый элемент рейтинга: "))

i = 0

while True:
    if new_element > rating_initial[i]:
        rating_initial.insert(i, new_element)
        print("Обновленный рейтинг:", rating_initial)
        break
    elif new_element <= rating_initial[-1]:
        rating_initial.append(new_element)
        print("Обновленный рейтинг:", rating_initial)
        break
    elif new_element <= rating_initial[i]:
        i = i + 1
        continue
    elif new_element > rating_initial[i]:
        rating_initial.insert(i, new_element)
        print("Обновленный рейтинг:", rating_initial)
        break
