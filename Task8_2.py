class MyOwnErr(Exception):

    def __init__(self, text):
        self.text = text


num_1 = input("Enter number 1: ")
num_2 = input("Enter number 2: ")

try:
    num_1 = float(num_1)
    num_2 = float(num_2)
    if num_2 == 0:
        raise MyOwnErr("Division by zero, number 2 should not be 0")
except (ValueError, MyOwnErr) as err:
    print(err)
else:
    print(f"число 1 / число 2 = {num_1 / num_2:.4f}")
