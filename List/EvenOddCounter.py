list = [1, 2, 3, 4, 5, 10, 20]
Even = 0
Odd = 0
for i in list:
    if i % 2 == 0:
        Even += 1
    else:
        Odd += 1
print(f"Odd: {Odd}")
print(f"Even: {Even}")
