list_of_numbers = [4 ,5, 9, 10, 13, 15, 18, 20]
print("For Loop...")
for i in list_of_numbers:
    if i > 10:
        print(f"{i} is greater than 10")
print("While Loop...")
i = 0
while i != len(list_of_numbers):
    if list_of_numbers[i] > 10:
        print(f"{list_of_numbers[i]} is greater than 10.")
    i += 1
