numbers = [-1, 2, -3, 4, -5, 6]
posNumbers = []
filter = lambda : [posNumbers.append(i) if i >= 0 else None for i in numbers]
filter()
print(posNumbers)
