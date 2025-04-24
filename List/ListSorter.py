list = [9, 65, 74, 10, 6, 4]
temp_list = list.copy()
sorted_list = []
for j in range(len(list)):
    max = temp_list[0]
    for i in range(1, len(temp_list)-1):
        if max < temp_list[i]:
            max = temp_list[i]
    sorted_list.append(max)
    temp_list.remove(max)      
print(sorted_list)
