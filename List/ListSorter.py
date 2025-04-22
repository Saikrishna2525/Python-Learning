list = [3, 1, 2]
list = [9, 65, 74, 10, 6, 4]
maximum = list[0]
minimum = list[0]
for i in range(len(list)-1):
    if not maximum > list[i+1]:
        maximum = list[i+1]
print(f"Max: {maximum}")
