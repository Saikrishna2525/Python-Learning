# 1. Square of Even Numbers
# Write a lambda function that takes a list of integers and returns a list of the squares of even numbers only.

# Example Input:
# numbers = [1, 2, 3, 4, 5, 6]
# Expected Output:
# [4, 16, 36]
numbers = [1, 2, 3, 4, 5, 6]
evnumbers = []
for i in numbers:
    if i % 2 == 0:
        evnumbers.append(i)
sqnumbers = []
square = [lambda x=x: sqnumbers.append(x ** 2) for x in evnumbers]
for i in square:
    i()
print(sqnumbers)
