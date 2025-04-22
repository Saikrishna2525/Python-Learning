list_with_duplicates = [1, 3, 5, 4, 5, 5, 6, 2, 6, 89, 0, 89]
duplicates = []
for i in list_with_duplicates:
    if list_with_duplicates.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)
print(duplicates)
