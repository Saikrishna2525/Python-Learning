list = [1, 2, 3, 4, 5,2,6]
Sums = []
for i in range(len(list)):
    for j in range(len(list)):
        if list[i] + list[j] == 5:
            Sums.append((list[i], list[j]))
for i in range(list.count(5)):
    Sums.append(5) 
print(Sums)
