import random

text_file = open("Text_5.txt", "w+", encoding="utf-8")

text_file.write(f"{random.randint(0, 100)} {random.randint(0, 100)} {random.randint(0, 100)} {random.randint(0, 100)} "
                f"{random.randint(0, 100)} {random.randint(0, 100)}")

text_file.seek(0)
read_text = text_file.read()
list = read_text.split(" ")

total_1 = 0
for i in list:
    total_1 = total_1 + int(i)

print("Сумма чисел из файла .txt =", total_1)

text_file.close()
