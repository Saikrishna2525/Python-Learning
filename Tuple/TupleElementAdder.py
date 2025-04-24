oldTuple1 = (1, 2, 3, 4, 5)
oldTuple1 = list(oldTuple1)
for i in range(oldTuple1[-1], 11):
    oldTuple1.append(i)
oldTuple1 = tuple(oldTuple1)
print(oldTuple1)
