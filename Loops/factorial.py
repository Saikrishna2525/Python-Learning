number = int(input("Enter the number which you want to find factorial for: "))
print("For Loop...")
factorial = 1
for i in range(1, number+1):
    factorial *= i
print(f"The factorial of {number} is {factorial}")
print("While Loop...")
factorial = 1
i = 1
while i != number+1:
    factorial *= i
    i += 1
print(f"The factorial of {number} is {factorial}.")
