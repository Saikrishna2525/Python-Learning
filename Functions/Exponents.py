def power(base, exponent):
    return 1 if exponent == 0 else base * power(base, exponent - 1)
print(power(int(input("Enter the base: ")), int(input("Enter the exponent: "))))