list_numbers = [1, 3, 5, 4, 5, 5, 6, 2, 6, 89, 0, 89]
even = []
odd = []
for i in list_numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"Odd: {odd}")
print(f"Even: {even}")
