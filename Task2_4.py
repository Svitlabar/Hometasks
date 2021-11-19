phrase = input("Введите предложение из нескольких слов, разделенных пробелами: \n")

var1 = phrase.split(" ")

for i, v in enumerate(var1, 1):
    print(f"{i}. {v[0:9]}")
