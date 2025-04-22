riddle_list = [2, 3, 2, 4, 4]
empty_set = set({})
for i in riddle_list:
    if i in empty_set:
        empty_set.discard(i)
    else:
        empty_set.add(i)
print(f"{empty_set} is/are unique number(s) in the list.")
