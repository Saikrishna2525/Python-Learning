riddle_list = [2, 3, 2, 4, 4, 4]
Unique_Values = []
temp_list = riddle_list.copy()
for i in temp_list:
    if temp_list.count(i) > 1:
        while i not in temp_list:
            temp_list.remove(i)
    if temp_list.count(i) == 1:
        Unique_Values.append(i)
print(f"The Unique Values are {Unique_Values}")   
