for j in range(1, 6):
    for i in range(1, 6):
        print(i*j, end=" ")
    print()

count = 1
for i in range(5):  # Two rows
    for j in range(5):  # Five columns
        print(f"{count:^3}", end='')  # ^3 centers the number in a 3-character wide field
        count += 1
    print()
