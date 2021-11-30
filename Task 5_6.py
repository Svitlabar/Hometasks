text_file = open("text_6.txt", "r", encoding="utf-8")

read_text = text_file.readlines()

values_list = []
key_list = []
for line in read_text:
    line_list = line.split(" ")

    total_hours = 0
    new_list = [[int(word.replace("(л)", "")) for word in line_list if "(л)" in word],
                [int(word.replace("(лаб)", "")) for word in line_list if "(лаб)" in word],
                [int(word.replace("(пр)", "")) for word in line_list if "(пр)" in word]]

    values_list = values_list + [sum([total_hours + sum(i) for i in new_list])]

    key_list = key_list + [line_list[0].replace(":", "")]

my_dict = {k: v for k, v in zip(key_list, values_list)}
print(my_dict)

text_file.close()
