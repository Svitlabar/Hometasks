list_1 = [4, 5, 6, 3, 21, 57, 4, 66, 4, 3, 7, 88, 4, 57]

list_nonrepeated = [m for m in list_1 if list_1.count(m) == 1]
print(list_nonrepeated)
