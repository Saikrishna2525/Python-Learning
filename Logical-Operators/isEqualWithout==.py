number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))
if number2 > number1:
    print(f"{number2} is greater than {number1}.")
elif number1 > number2:
    print(f"{number1} is greater than {number2}.")
else:
    print("Both numbers are equal.")
