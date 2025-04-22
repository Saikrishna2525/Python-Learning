list1 = [5, 9, 3, 9, 4, 1, 4]
list2 = [4, 5, 5, 4, 1, 3, 8]
list1.extend(list2)
print(list1)
for i in list1:
    while list1.count(i) != 1:
        list1.remove(i)
print(list1)
