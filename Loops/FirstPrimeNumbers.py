number = int(input("Until which number you want to find Prime Numbers: "))
for i in range(1, number+1):
    factors = []
    for j in range(1, i+1):
        if i % j == 0:
            factors.append(j)
    if len(factors) == 2:
        print(f"{i} is a prime number.")
