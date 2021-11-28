from functools import reduce

list_even = [m for m in range(100, 1001, 2)]
print(list_even)


def multiply_even(a, b):
    return a * b


print(reduce(multiply_even, list_even))
