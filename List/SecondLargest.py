list = [9, 65, 74, 10, 6, 4]
temp_list = list.copy()
maximum = list[0]
for i in range(len(list)-1):
    if not maximum > list[i+1]:
        maximum = list[i+1]
temp_list.remove(maximum)
maximum = temp_list[0]
for i in range(len(temp_list)-1):
    if not maximum > temp_list[i+1]:
        maximum = temp_list[i+1]
print(f"Second Max: {maximum}")