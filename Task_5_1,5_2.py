text_file = open("Text_file1.txt", "w+", encoding="utf-8")

print("Для завершения ввода текста оставьте пустую строку")

while True:
    text_input = input("Введите текст строки: ")
    if text_input == "":
        print("\nВвод текста завершен\n")
        break
    else:
        text_file.write(f"{text_input}\n")
        continue

text_file.seek(0)

read_text = text_file.readlines()
print("Количество строк : ", len(read_text))
for i in read_text:
    line_list = i.split(" ")
    word_number = len(line_list) - line_list.count('') - line_list.count('\n') - line_list.count('-')
    print("Количество слов в строке", (read_text.index(i) + 1), ": ", word_number)

text_file.close()
