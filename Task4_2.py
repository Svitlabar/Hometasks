list_numbers = [11, 88, 22, 55, 24, 332, 5587, 41, 587, 54, 60, 61, 88, 32]

list_1 = [print(list_numbers[i]) for i in range(1, len(list_numbers)) if list_numbers[i] > list_numbers[i-1]]
