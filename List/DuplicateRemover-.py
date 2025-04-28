list_with_duplicates = [5, 10, 3, 4, 10, 1, 4, 0, 5, 0, 1, 3, 8,1]
list_without_duplicates = []
for i in list_with_duplicates:
    if i not in list_without_duplicates:
        list_without_duplicates.append(i)
print(list_without_duplicates)
