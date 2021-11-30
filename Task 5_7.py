import json

with open("text_7.txt", "r", encoding="utf-8") as text_file:
    read_text = text_file.readlines()

list_keys = []
list_values = []
average_profit = 0
i = 0
for line in read_text:
    line_list = line.split(" ")
    profit = int(line_list[2]) - int(line_list[3])
    if profit > 0:
        average_profit = average_profit + profit
        i += 1
    list_keys = list_keys + [" ".join([line_list[0], line_list[1]])]
    list_values = list_values + [profit]

list_result = [{k: v for k, v in zip(list_keys, list_values)}, {"average_profit": average_profit / i}]
print(list_result)

data = [
    {
        k: v for k, v in zip(list_keys, list_values)
    },
    {
        "average_profit": average_profit / i
    }
]

with open("text_77.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file)


