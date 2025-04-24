t1 = (1, 2, 3, 4,8)
t2 = (1, 5, 3, 8)
match = 0
for i in range(len(t1)-1):
    if t1[i] == t2[i]: 
        match += 1
print(f"{match} numbers match in both tuples")
