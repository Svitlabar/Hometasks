text_file = open("text_4.txt", "r", encoding="utf-8")
text_filenew = open("text_4new.txt", "w", encoding='utf-8')

for i in range(1, 5):
    line = text_file.readline()
    text_filenew.write(line.replace("One", "Один")) if line.count("One") >= 1 else False
    text_filenew.write(line.replace("Two", "Два")) if line.count("Two") >= 1 else False
    text_filenew.write(line.replace("Three", "Три")) if line.count("Three") >= 1 else False
    text_filenew.write(line.replace("Four", "Четыре")) if line.count("Four") >= 1 else False

text_filenew.close()

text_file.close()
