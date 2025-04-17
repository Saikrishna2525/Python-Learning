# check if a number is prime or not a prime number.
number = int(input("Please Enter your number: "))
numbers = []
for i in reversed(range(number, 0, -1)):
    numbers.insert(0, i)
factors = []
for i in numbers:
    if number % i == 0:
        factors.insert(0, i)
if len(factors) > 2:
    print(f"{number} is a composite number!")
elif len(factors) == 2:
    print(f"{number} is a prime number!")
else:
    print("Your number is neither positive nor negative as it is 1")