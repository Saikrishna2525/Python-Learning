numbers = [1, 2, 3, 4]
double = [lambda i=i: i * 2 for i in numbers]
for m in double:
    print(m())
