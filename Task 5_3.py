text_file = open("text_3.txt", "r", encoding="utf-8")

read_text = text_file.readlines()
total_salary = 0
print("Число сотруднико с зарплатой менее 20000.0: \n")

for line in read_text:
    line_list = line.split(" ")
    total_salary = total_salary + float(line_list[1].replace("\n", ""))
    print(line_list[0]) if float(line_list[1]) < 20000 else False
average_salary = total_salary / len(read_text)
print(f"\nСредняя величина дохода сотрудников = {average_salary:.2f}")

text_file.close()
