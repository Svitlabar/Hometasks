from itertools import count, cycle

# 1 часть

for n in count(11):
    if n > 21:
        break
    else:
        print(n)

# 2 часть
print("\n")

i = 0
for m in cycle(["Ram", "--pam", "----pam"]):
    if i > 11:
        break
    print(m)
    i += 1
