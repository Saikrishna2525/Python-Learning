tuple_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple_numbers = list(tuple_numbers)
K = int(input("K = "))
for i in range(K):
    tuple_numbers.insert(0, tuple_numbers.pop(-1)) 
tuple_numbers = tuple(tuple_numbers)
print(tuple_numbers)
