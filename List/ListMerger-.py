list1 = [5, 9, 3, 9, 4, 1, 4]
list2 = [4, 5, 5, 4, 1, 3, 8,3]
list1.extend(list2)
list2.clear()
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
