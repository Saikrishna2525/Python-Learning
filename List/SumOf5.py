list = [1, 2, 3, 4, 5,2,6]
Sums = []
for i in range(len(list)):
    if list[i] == 5:
        Sums.append(5)
    else:
        for j in range(i, len(list)-1):
            if i + j == 5:
                Sums.append((i, j))
print(Sums)
