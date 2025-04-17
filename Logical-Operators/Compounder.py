from os import system
number1 = input("Please Enter first number: ")
number2 = input("Please Enter second number: ")
if (number1 == number1.lower() and number1 == number1.upper()) and (number2 == number2.lower() == number2.upper()):
    system("cls")
    number1 = float(number1)
    number2 = float(number2)
    print(f"{number1} raised to the power of {number2} is {number1 ** number2}")
else:
    print("Your number must contain only numbers")