list_duplicates = [2, 3, 2, 4, 4]
set_duplicates = set(list_duplicates)
deletions_required = len(list_duplicates) - len(set_duplicates)
print(f"{deletions_required} deletions are required.")
