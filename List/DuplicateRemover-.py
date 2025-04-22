list_with_duplicates = [5, 10, 3, 4, 10, 1, 4, 0, 5, 0, 1, 3, 8]
for i in list_with_duplicates:
    print(list_with_duplicates.count(i) != 1, "|", i)
    while list_with_duplicates.count(i) != 1 or list_with_duplicates.count(i) == 2:
        del list_with_duplicates[list_with_duplicates.index(i)]
print(list_with_duplicates)
