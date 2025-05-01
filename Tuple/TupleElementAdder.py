oldTuple = (1, 2, 3, 4, 5)
newTuple = []
for i in oldTuple:
    newTuple.append(i)
for i in range(newTuple[-1] + 1, 11):
    newTuple.append(i)
newTuple = tuple(newTuple)
print(newTuple)
