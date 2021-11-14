income1 = int(input("Введите сумму выручки, EUR: "))
costs = int(input("Введите сумму издержек, EUR: "))

profit = income1 - costs

if profit > 0:
    profitability = profit / income1 * 100
    print(f"Финансовые показатели: работа в прибыль, рентабельность: {profitability:.2f} %")
    numb_employees = int(input("Введите численность сотрудников фирмы: "))
    profit_1employee = profit / numb_employees
    print(f"Прибыль на одного сотрудника: {profit_1employee:.2f} EUR")
if profit < 0:
    print("Финансовые показатели: работа в убыток")
if profit == 0:
    print("Финансовые показатели: выход в 0")
